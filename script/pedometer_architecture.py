import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(36, 26))
ax.set_xlim(0, 36)
ax.set_ylim(0, 26)
ax.axis('off')
fig.patch.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')

C = {
    'android':  '#3DDC84',
    'ios':      '#4BA3F5',
    'rn':       '#61DAFB',
    'store':    '#FF6B6B',
    'service':  '#FFE66D',
    'ui':       '#98E8C1',
    'db_a':     '#4CAF50',
    'db_i':     '#2196F3',
    'text_h':   '#F0F6FC',
    'text_s':   '#8B949E',
    'arrow_a':  '#3DDC84',
    'arrow_i':  '#4BA3F5',
    'arrow_e':  '#FFA657',
    'arrow_g':  '#58A6FF',
    'fg_svc':   '#C792EA',
    'midnight': '#98E8C1',
    'reboot':   '#FFB347',
    'border':   '#30363D',
}

def box(ax, x, y, w, h, color, alpha=0.18, radius=0.25, lw=1.8, edge_color=None):
    ec = edge_color or color
    patch = FancyBboxPatch((x, y), w, h,
                           boxstyle=f"round,pad=0.04,rounding_size={radius}",
                           facecolor=color, alpha=alpha,
                           edgecolor=ec, linewidth=lw, zorder=2)
    ax.add_patch(patch)

def t(ax, x, y, text, size=8.5, color='white', bold=False, ha='center', va='center', zorder=5, wrap=False):
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, fontsize=size, color=color, fontweight=weight,
            ha=ha, va=va, zorder=zorder, fontfamily='monospace')

def arr(ax, x1, y1, x2, y2, color, lw=2.0, dashed=False, label=''):
    style = '--' if dashed else '-'
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                linestyle=style,
                                connectionstyle='arc3,rad=0.0'),
                zorder=6)
    if label:
        mx, my = (x1+x2)/2 + 0.1, (y1+y2)/2
        ax.text(mx, my, label, fontsize=6.5, color=color, ha='left', va='center',
                fontfamily='monospace', zorder=7,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='#0D1117',
                          alpha=0.85, edgecolor='none'))

def section_label(ax, x, y, text, color, size=8.5):
    ax.text(x, y, text, fontsize=size, color=color, fontweight='bold',
            ha='center', va='center', fontfamily='monospace', zorder=8,
            bbox=dict(boxstyle='round,pad=0.3', facecolor=color, alpha=0.15,
                      edgecolor=color, linewidth=1.2))

# ========================================================
# LAYER BANDS (bottom to top)
# ========================================================
bands = [
    # y_bot, height, color, label, alpha
    (0.3,  1.8,  '#3DDC84', 'HARDWARE / OS SENSOR LAYER',             0.05),
    (2.2,  6.4,  '#FFFFFF', 'NATIVE LAYER  (Android Kotlin + iOS Swift)', 0.03),
    (8.7,  1.3,  '#61DAFB', 'REACT NATIVE BRIDGE  (NativeModules / NativeEventEmitter)', 0.07),
    (10.1, 2.1,  '#FFE66D', 'JS SERVICE LAYER',                       0.06),
    (12.3, 2.6,  '#FF6B6B', 'STATE MANAGEMENT  (External Store + Redux + AppState)', 0.06),
    (15.0, 2.1,  '#98E8C1', 'REACT CONTEXT / PROVIDER',               0.07),
    (17.2, 2.1,  '#F0F6FC', 'UI COMPONENTS',                          0.04),
]
for yb, yh, bc, bl, ba in bands:
    box(ax, 0.3, yb, 35.4, yh, bc, alpha=ba, radius=0.4, lw=0.8, edge_color='#30363D')
    t(ax, 18.0, yb + yh - 0.28, bl, size=8, color='#8B949E', bold=True)

# ========================================================
# TITLE
# ========================================================
t(ax, 18, 25.4, 'SmartWell Pedometer  —  Full Architecture Diagram', size=17, bold=True, color=C['text_h'])
t(ax, 18, 24.95, 'Android (Kotlin)  |  iOS (Swift + ObjC)  |  React Native  |  useSyncExternalStore  |  Redux', size=10, color=C['text_s'])

# ========================================================
# L0: HARDWARE
# ========================================================
# Android Sensor
box(ax, 0.8, 0.5, 7.0, 1.2, C['android'], alpha=0.35, lw=2.5)
t(ax, 4.3, 1.18, 'TYPE_STEP_COUNTER', size=10, bold=True, color=C['android'])
t(ax, 4.3, 0.82, 'Android Hardware Sensor (SensorManager)', size=8, color=C['text_s'])

# iOS CMPedometer
box(ax, 8.5, 0.5, 8.0, 1.2, C['ios'], alpha=0.35, lw=2.5)
t(ax, 12.5, 1.18, 'CMPedometer', size=10, bold=True, color=C['ios'])
t(ax, 12.5, 0.82, 'CoreMotion Framework  (iOS 8+)', size=8, color=C['text_s'])

# ========================================================
# L1: NATIVE — ANDROID (left column)
# ========================================================
# Android section bg
box(ax, 0.5, 2.3, 16.5, 6.3, C['android'], alpha=0.05, lw=1.2, edge_color=C['android'])
section_label(ax, 8.75, 8.45, '  Android (Kotlin)  ', C['android'], size=8)

# StepCounterManager
box(ax, 0.7, 5.6, 7.2, 2.8, C['android'], alpha=0.3, lw=2.2)
t(ax, 4.3, 8.15, 'StepCounterManager', size=10, bold=True, color=C['android'])
t(ax, 4.3, 7.85, '(Singleton — shared Module + Service)', size=7.5, color=C['text_s'])
mgr_items = [
    'initialize()              — load baseline from DB, register sensor',
    'onSensorChanged()         — real-time sensor events',
    'getTodaySteps()           — stepOffset + (sensor - baseline)',
    'handleDateChange()        — midnight save + reset (1-min timer)',
    'handleRebootDetection()   — sensor drop → restore from DB',
    'addCallback() / removeCallback()',
]
for i, m in enumerate(mgr_items):
    t(ax, 4.3, 7.52 - i*0.32, m, size=7.2, color=C['text_h'])

# AOSPedometerModule
box(ax, 0.7, 2.5, 7.2, 2.9, C['android'], alpha=0.3, lw=2.2)
t(ax, 4.3, 5.15, 'AOSPedometerModule', size=10, bold=True, color=C['android'])
t(ax, 4.3, 4.85, '(RCTBridgeModule — exposed to JS)', size=7.5, color=C['text_s'])
module_items = [
    'loadTodaySteps()          — load + emit StepUpdate',
    'startUpdates()            — enable real-time sensor',
    'stopUpdates()             — disable sensor (if no FG Svc)',
    'fetchDailySteps(s, e)     — query from Room DB',
    'startStepCounterService() — start Foreground Service',
    'stopStepCounterService()  — stop Foreground Service',
    'getServiceStatus()        — { isServiceRunning, currentSteps }',
]
for i, m in enumerate(module_items):
    t(ax, 4.3, 4.52 - i*0.32, m, size=7.0, color=C['text_h'])

# PedometerService (Foreground)
box(ax, 8.2, 4.3, 8.5, 4.2, C['fg_svc'], alpha=0.22, lw=2.2)
t(ax, 12.45, 8.26, 'PedometerService', size=10, bold=True, color=C['fg_svc'])
t(ax, 12.45, 7.97, '(Android Foreground Service — HEALTH type)', size=7.5, color=C['text_s'])
fg_items = [
    'onCreate()       — create notification channels',
    'onStartCommand() — init StepCounterManager + callbacks',
    'startForeground(FOREGROUND_SERVICE_TYPE_HEALTH)',
    'updateSteps()    — update notification with new steps',
    'createNotification() — custom RemoteViews layout',
    '  "Earn" button  deeplink: smartwel://walkingBokji',
    'schedulePeriodicRestart() — AlarmManager every 5 min',
    'BootReceiver     — auto-restart after device reboot',
    'ServiceRestartReceiver — re-start on alarm fire',
]
for i, m in enumerate(fg_items):
    t(ax, 12.45, 7.64 - i*0.32, m, size=7.0, color=C['text_h'])

# Room DB
box(ax, 8.2, 2.5, 8.5, 1.65, C['db_a'], alpha=0.32, lw=2.2)
t(ax, 12.45, 3.89, 'Room DB  (step_counter_database_v2)', size=9.5, bold=True, color=C['db_a'])
t(ax, 12.45, 3.60, 'DailyStepsEntity { date: String, todaySteps: Long,', size=7.2, color=C['text_h'])
t(ax, 12.45, 3.30, '                   sensorSteps: Long, timestamp: Long }', size=7.2, color=C['text_h'])
t(ax, 12.45, 2.98, 'StepCounterRepository: initializeTodayData · saveTodaySteps · getDailyStepsInRange', size=6.8, color=C['text_s'])

# ========================================================
# L1: NATIVE — iOS (right column)
# ========================================================
box(ax, 17.5, 2.3, 18.2, 6.3, C['ios'], alpha=0.05, lw=1.2, edge_color=C['ios'])
section_label(ax, 26.6, 8.45, '  iOS (Swift + ObjC)  ', C['ios'], size=8)

# IOSPedometerModule
box(ax, 17.7, 4.1, 11.0, 4.4, C['ios'], alpha=0.28, lw=2.2)
t(ax, 23.2, 8.25, 'IOSPedometerModule.swift', size=10, bold=True, color=C['ios'])
t(ax, 23.2, 7.96, '(RCTEventEmitter + subclassed)', size=7.5, color=C['text_s'])
ios_items = [
    'loadTodaySteps()   CMPedometer.queryPedometerData(00:00~now)',
    '                    → set todaySteps, reset liveSteps',
    '                    → save to Core Data, emit StepUpdate',
    'startUpdates()     CMPedometer.startUpdates(from: now)',
    '                    → baselineLiveSteps = first value',
    '                    → liveSteps = sensorVal - baseline',
    '                    → emit StepUpdate (todaySteps + liveSteps)',
    '                    → auto-save every 10 steps',
    'stopUpdates()      todaySteps += liveSteps; reset liveSteps',
    'fetchDailySteps()  Core Data query + in-memory merge (today)',
    'saveTodaySteps()   Core Data persist',
    'State: todaySteps · liveSteps · baselineLiveSteps: Int',
]
for i, m in enumerate(ios_items):
    t(ax, 23.2, 7.61 - i*0.30, m, size=7.0, color=C['text_h'])

# Core Data
box(ax, 17.7, 2.5, 11.0, 1.45, C['db_i'], alpha=0.32, lw=2.2)
t(ax, 23.2, 3.68, 'Core Data  (DailySteps)', size=9.5, bold=True, color=C['db_i'])
t(ax, 23.2, 3.37, 'DailySteps { date: Date?, steps: Int64 }', size=7.5, color=C['text_h'])
t(ax, 23.2, 3.08, 'fetchByDateRange() · save() · merge memory+DB · auto-save every 10 steps', size=6.8, color=C['text_s'])

# IOSPedometer.m (ObjC bridge)
box(ax, 29.2, 4.1, 5.9, 4.4, C['ios'], alpha=0.2, lw=2.2)
t(ax, 32.15, 8.25, 'IOSPedometer.m', size=9.5, bold=True, color=C['ios'])
t(ax, 32.15, 7.96, '(Objective-C Bridge)', size=7.5, color=C['text_s'])
objc = [
    'RCT_EXTERN_MODULE',
    '  IOSPedometerModule',
    '  RCTEventEmitter',
    '',
    'RCT_EXTERN_METHOD:',
    '  loadTodaySteps',
    '  startUpdates',
    '  stopUpdates',
    '  fetchDailySteps',
    '  saveTodaySteps',
]
for i, m in enumerate(objc):
    t(ax, 32.15, 7.60 - i*0.32, m, size=7.0, color=C['text_h'])

# ========================================================
# L2: RN BRIDGE
# ========================================================
box(ax, 0.6, 8.8, 7.5, 0.9, C['android'], alpha=0.35, lw=2.2)
t(ax, 4.35, 9.25, 'NativeModules.AOSPedometerModule', size=8.5, bold=True, color=C['android'])

box(ax, 8.8, 8.8, 9.5, 0.9, C['arrow_e'], alpha=0.35, lw=2.2)
t(ax, 13.55, 9.25, 'NativeEventEmitter  >>>  event: "StepUpdate"', size=8.5, bold=True, color=C['arrow_e'])

box(ax, 19.0, 8.8, 11.5, 0.9, C['ios'], alpha=0.35, lw=2.2)
t(ax, 24.75, 9.25, 'NativeModules.IOSPedometerModule', size=8.5, bold=True, color=C['ios'])

# ========================================================
# L3: JS SERVICE
# ========================================================
box(ax, 0.6, 10.2, 12.5, 1.8, C['service'], alpha=0.3, lw=2.2)
t(ax, 6.85, 11.72, 'PedometerService.ts  (Platform-Agnostic JS Wrapper)', size=9.5, bold=True, color=C['service'])
t(ax, 6.85, 11.43, 'loadTodaySteps  ·  startUpdates  ·  stopUpdates  ·  fetchDailySteps  ·  checkPermissionStatus  ·  requestPermission  ·  getEventEmitter()', size=7, color=C['text_h'])
t(ax, 6.85, 11.12, 'Platform.OS === "android"  ->  AOSPedometerModule     else  ->  IOSPedometerModule', size=7, color=C['text_s'])
t(ax, 6.85, 10.82, 'checkPermissionStatus: Android = PermissionsAndroid.check(ACTIVITY_RECOGNITION)  |  iOS = loadTodaySteps() try/catch', size=6.8, color=C['text_s'])

box(ax, 13.6, 10.2, 9.5, 1.8, C['fg_svc'], alpha=0.28, lw=2.2)
t(ax, 18.35, 11.72, 'ForegroundServiceUtils.ts  (Android Only)', size=9.5, bold=True, color=C['fg_svc'])
t(ax, 18.35, 11.43, 'startService()   ->  startStepCounterService()', size=7.5, color=C['text_h'])
t(ax, 18.35, 11.15, 'stopService()    ->  stopStepCounterService()', size=7.5, color=C['text_h'])
t(ax, 18.35, 10.87, 'getServiceStatus()  ->  { isServiceRunning: Bool, currentSteps: Int }', size=7.2, color=C['text_s'])

box(ax, 23.6, 10.2, 11.9, 1.8, C['rn'], alpha=0.28, lw=2.2)
t(ax, 29.55, 11.72, 'Permission Handling', size=9.5, bold=True, color=C['rn'])
t(ax, 29.55, 11.43, 'Android: PermissionsAndroid.request(ACTIVITY_RECOGNITION)', size=7.5, color=C['text_h'])
t(ax, 29.55, 11.15, 'iOS:     CMPedometer auto-prompt on first queryPedometerData()', size=7.5, color=C['text_h'])
t(ax, 29.55, 10.87, 'openAppSettings() when "never_ask_again" selected', size=7.2, color=C['text_s'])

# ========================================================
# L4: STATE MANAGEMENT
# ========================================================
box(ax, 0.6, 12.4, 12.5, 2.4, C['store'], alpha=0.28, lw=2.2)
t(ax, 6.85, 14.54, 'pedometerStore.ts', size=10, bold=True, color=C['store'])
t(ax, 6.85, 14.25, '(External Singleton — useSyncExternalStore)', size=7.5, color=C['text_s'])
store_items = [
    'setSteps(next: number)   Throttle 100ms max 1 re-render',
    '  if now - lastUpdate >= 100ms  ->  immediate _updateSteps()',
    '  else schedule setTimeout for remaining time',
    'getSnapshot(): number    current steps (snapshot)',
    'subscribe(fn): () => void   register / unregister listener',
    'reset()                  clear steps to 0',
]
for i, m in enumerate(store_items):
    t(ax, 6.85, 13.92 - i*0.27, m, size=7.2, color=C['text_h'])

box(ax, 13.6, 12.4, 10.0, 2.4, '#FF9E9E', alpha=0.22, lw=2.2)
t(ax, 18.6, 14.54, 'Redux: pedometerSlice', size=10, bold=True, color='#FF9E9E')
t(ax, 18.6, 14.25, '(Low-frequency company permission state only)', size=7.5, color=C['text_s'])
redux_items = [
    'state: {',
    '  isInitialized: boolean,',
    '  pedometer_user_seq: number',
    '}',
    'setIsInitialized(isInitialized, user_seq)',
    'clearPedometerAllowed()  — on logout',
]
for i, m in enumerate(redux_items):
    t(ax, 18.6, 13.92 - i*0.27, m, size=7.2, color=C['text_h'])

box(ax, 24.1, 12.4, 11.4, 2.4, C['rn'], alpha=0.22, lw=2.2)
t(ax, 29.8, 14.54, 'AppState Listener  (React Native)', size=10, bold=True, color=C['rn'])
appstate_items = [
    '"active"     ->  check company flag',
    '             ->  loadTodaySteps + startUpdates',
    '             ->  setIsUpdatesActive(true)',
    '"inactive"   ->  PedometerService.stopUpdates()',
    '             ->  Android: Foreground Service keeps sensor alive',
    '             ->  setIsUpdatesActive(false)',
]
for i, m in enumerate(appstate_items):
    t(ax, 29.8, 13.92 - i*0.27, m, size=7.2, color=C['text_h'])

# ========================================================
# L5: PROVIDER
# ========================================================
box(ax, 0.6, 15.1, 34.9, 1.8, C['ui'], alpha=0.22, lw=2.2)
t(ax, 18.05, 16.65, 'PedometerProvider.tsx  —  React Context + Lifecycle Orchestrator', size=10, bold=True, color=C['ui'])
t(ax, 18.05, 16.37, 'Context API: { isLoading: bool, hasPermission: bool, loadTodaySteps, saveTodaySteps, fetchDailySteps, checkPermissionStatus, requestPermission }', size=7.5, color=C['text_h'])
lifecycle = ('useEffect([user]):  1) check user.swmng_pedometer===1  '
             '2) checkPermissionStatus  3) setupStepsListener (StepUpdate->pedometerStore.setSteps)  '
             '4) loadTodaySteps  5) startUpdates  6) startForegroundService[Android]  |  '
             'cleanup: remove listeners, stopUpdates if no Foreground Service')
t(ax, 18.05, 15.98, lifecycle, size=6.8, color=C['text_s'])
t(ax, 18.05, 15.7, 'swmng_pedometer flag checked BEFORE every native call — gates all pedometer functionality per company', size=7, color='#FFB347')

# ========================================================
# L6: UI
# ========================================================
ui_boxes = [
    (0.7,  17.3, 5.5, 1.8, 'StepCounterWidget\n(Walking Home Screen)'),
    (6.6,  17.3, 6.5, 1.8, 'WalkingWelfareScreen\n(Daily stats + ranking)'),
    (13.5, 17.3, 6.0, 1.8, 'PedometerSettings\n(Permission request UI)'),
    (19.9, 17.3, 5.5, 1.8, 'HomeTab StepBanner\n(Live step display)'),
]
for bx, by, bw, bh, btitle in ui_boxes:
    box(ax, bx, by, bw, bh, C['ui'], alpha=0.28, lw=2.0)
    t(ax, bx+bw/2, by+bh/2, btitle, size=8, color=C['text_h'])

# useSyncExternalStore call-out
box(ax, 25.8, 17.3, 9.7, 1.8, '#FFD700', alpha=0.25, lw=2.5, edge_color='#FFD700')
t(ax, 30.65, 18.55, 'useSyncExternalStore(', size=8.5, bold=True, color='#FFD700')
t(ax, 30.65, 18.22, '  pedometerStore.subscribe,', size=8, color='#FFD700')
t(ax, 30.65, 17.90, '  pedometerStore.getSnapshot', size=8, color='#FFD700')
t(ax, 30.65, 17.60, ')  ->  steps: number', size=8, color='#FFD700')

# ========================================================
# CALLOUT BOXES (right side, native layer)
# ========================================================
# Reboot Recovery
box(ax, 30.0, 5.8, 5.7, 2.6, C['reboot'], alpha=0.2, lw=1.8, edge_color=C['reboot'])
t(ax, 32.85, 8.18, '[Reboot Recovery]', size=8.5, bold=True, color=C['reboot'])
rb = [
    'sensor < baseline?',
    '=> reboot detected',
    '=> load DB lastSteps',
    '=> stepOffset = lastSteps',
    '=> baseline = new value',
    'steps = offset+(sensor-base)',
]
for i, m in enumerate(rb):
    t(ax, 32.85, 7.85 - i*0.33, m, size=7, color=C['reboot'])

# Midnight reset
box(ax, 30.0, 2.5, 5.7, 3.1, C['midnight'], alpha=0.2, lw=1.8, edge_color=C['midnight'])
t(ax, 32.85, 5.35, '[Midnight Reset]', size=8.5, bold=True, color=C['midnight'])
mn = [
    '1-min timer + date check',
    '=> save yesterday final',
    '=> reset baseline+offset',
    '=> init new day DB row',
    '=> onNewDayDetected()',
    '(Android StepCounterManager)',
]
for i, m in enumerate(mn):
    t(ax, 32.85, 5.0 - i*0.33, m, size=7, color=C['midnight'])

# ========================================================
# ARROWS
# ========================================================
# Hardware -> Native
arr(ax, 4.3,  1.7,  4.3,  5.6,  C['android'], lw=2.2, label='onSensorChanged()')
arr(ax, 12.5, 1.7,  23.2, 4.1,  C['ios'],     lw=2.2, label='startUpdates / queryPedometerData')

# StepUpdate events (dashed)
arr(ax, 4.3,  2.5,  11.0, 8.8,  C['arrow_e'], lw=1.8, dashed=True, label='emit StepUpdate')
arr(ax, 23.2, 4.1,  16.5, 8.8,  C['arrow_e'], lw=1.8, dashed=True, label='emit StepUpdate')

# Module -> Foreground Service
arr(ax, 7.9,  4.0,  8.2,  5.5,  C['fg_svc'],  lw=1.8, label='startService')

# Module <-> StepCounterManager
arr(ax, 4.3,  5.6,  4.3,  5.45, C['android'], lw=1.5)
arr(ax, 4.3,  2.5,  8.2,  3.5,  C['db_a'],   lw=1.5, label='Repository.save')

# FG Service -> Room DB
arr(ax, 12.45, 4.3, 12.45, 4.15, C['db_a'], lw=1.5)

# iOS -> Core Data
arr(ax, 23.2, 4.1, 23.2, 3.95, C['db_i'], lw=1.5)

# Bridge -> JS Service
arr(ax, 4.35, 8.8, 5.0,  10.2, C['android'], lw=2.0)
arr(ax, 24.75, 8.8, 14.5, 10.2, C['ios'],    lw=2.0)
arr(ax, 13.55, 8.8, 8.0,  10.2, C['arrow_e'], lw=2.0, label='addListener(StepUpdate)')

# JS Service -> Provider
arr(ax, 6.85, 10.2, 9.0, 15.1, C['service'], lw=2.0)
arr(ax, 18.35, 10.2, 16.0, 15.1, C['fg_svc'], lw=1.8)

# StepUpdate -> Store
arr(ax, 8.0, 10.2, 6.85, 12.4, C['arrow_e'], lw=1.8, dashed=True, label='pedometerStore.setSteps()')

# Store -> UI
arr(ax, 6.85, 12.4, 30.65, 17.3, C['store'], lw=2.0, dashed=True)

# Redux -> Provider
arr(ax, 18.6, 12.4, 15.0, 15.1, '#FF9E9E', lw=1.5, label='swmng_pedometer gate')

# AppState -> Provider
arr(ax, 29.8, 12.4, 25.0, 15.1, C['rn'], lw=1.5, dashed=True, label='lifecycle events')

# Provider -> UI
arr(ax, 18.05, 15.1, 16.5, 17.3, C['ui'], lw=1.5)

# Permission -> Provider
arr(ax, 29.55, 10.2, 28.0, 15.1, C['rn'], lw=1.5, dashed=True)

# ========================================================
# LEGEND
# ========================================================
legend = [
    (C['android'], 'Android (Kotlin)'),
    (C['ios'],     'iOS (Swift)'),
    (C['rn'],      'React Native'),
    (C['service'], 'JS Service'),
    (C['store'],   'External Store'),
    (C['fg_svc'],  'Foreground Service'),
    (C['arrow_e'], 'StepUpdate Event'),
    (C['db_a'],    'Room DB'),
    (C['db_i'],    'Core Data'),
    ('#FFD700',    'useSyncExternalStore'),
]
lx_start = 0.8
for i, (lc, lt) in enumerate(legend):
    lxi = lx_start + i * 3.48
    patch = FancyBboxPatch((lxi, 19.55), 0.45, 0.45,
                           boxstyle='round,pad=0.03,rounding_size=0.08',
                           facecolor=lc, alpha=0.8,
                           edgecolor='white', linewidth=0.8, zorder=5)
    ax.add_patch(patch)
    t(ax, lxi + 0.6, 19.77, lt, size=7.5, color=C['text_s'], ha='left')

t(ax, 18, 19.25,
  '--- Solid arrow: direct method call     - - -  Dashed arrow: async event / callback     Arrow color = layer origin',
  size=7.5, color=C['text_s'])

# ========================================================
# SAVE
# ========================================================
output_path = '/Users/bizbee/ImageNotification/APPforMobile/pedometer_architecture.png'
plt.tight_layout(pad=0.3)
plt.savefig(output_path, dpi=160, bbox_inches='tight',
            facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f'Saved: {output_path}')
