import webview

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iOS 18 Pro Max - Ultimate Suite</title>
    <!-- FontAwesome & Leaflet Map CSS/JS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

    <style>
        :root {
            --ios-radius: 22%;
        }

        * {
            box-sizing: border-box;
            user-select: none;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Helvetica Neue", sans-serif;
        }

        body {
            background-color: #050505;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
        }

        .viewport-scaler {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            padding: 20px;
        }

        /* Chasis iPhone 15 Pro Max */
        .iphone-container {
            width: 390px;
            height: 844px;
            max-height: 95vh;
            aspect-ratio: 390 / 844;
            background: url('https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?q=80&w=1000&auto=format&fit=crop') center/cover;
            border-radius: 54px;
            position: relative;
            box-shadow: 0 0 0 10px #2a2a2b, 0 0 0 12px #181819, 0 25px 60px rgba(0,0,0,0.95);
            overflow: hidden;
            flex-shrink: 0;
        }

        /* Status Bar */
        .status-bar {
            position: absolute;
            top: 0;
            width: 100%;
            height: 46px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 24px;
            color: #fff;
            font-size: 14px;
            font-weight: 600;
            z-index: 100;
            cursor: pointer;
        }

        .status-icons { display: flex; gap: 6px; align-items: center; font-size: 12px; }

        /* Dynamic Island */
        .dynamic-island {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 34px;
            background-color: #000;
            border-radius: 20px;
            z-index: 120;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 10px;
            color: white;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            overflow: hidden;
        }

        .eq-bar-container { display: flex; gap: 2px; align-items: flex-end; height: 14px; }
        .eq-bar { width: 3px; background: #34c759; border-radius: 2px; animation: eqAnim 0.8s infinite ease-in-out alternate; }
        .eq-bar:nth-child(2) { animation-delay: 0.2s; }
        .eq-bar:nth-child(3) { animation-delay: 0.4s; }
        @keyframes eqAnim { 0% { height: 3px; } 100% { height: 14px; } }

        /* NOTIFICATION BANNER */
        .notif-banner {
            position: absolute;
            top: 10px;
            left: 12px;
            right: 12px;
            background: rgba(25, 25, 25, 0.92);
            backdrop-filter: blur(25px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px;
            padding: 12px 16px;
            color: white;
            z-index: 130;
            display: flex;
            align-items: center;
            gap: 12px;
            transform: translateY(-120%);
            opacity: 0;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .notif-banner.active { transform: translateY(0); opacity: 1; }

        /* CENTRO DE NOTIFICACIONES */
        .notif-center {
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.6);
            backdrop-filter: blur(35px);
            z-index: 95;
            padding: 60px 20px 20px 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
            transform: translateY(-100%);
            opacity: 0;
            transition: all 0.4s ease;
            color: white;
            pointer-events: none;
        }
        .notif-center.active { transform: translateY(0); opacity: 1; pointer-events: auto; }

        /* PANTALLA DE BLOQUEO */
        .lock-screen {
            position: absolute;
            inset: 0;
            z-index: 80;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            padding: 55px 20px 45px 20px;
            color: white;
            transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
            background: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=1000&auto=format&fit=crop') center/cover;
            cursor: pointer;
        }
        .lock-screen.unlocked { transform: translateY(-100%); opacity: 0; pointer-events: none; }
        .lock-clock { font-size: 86px; font-weight: 200; letter-spacing: -3px; line-height: 0.95; }
        .lock-widgets { display: flex; gap: 12px; background: rgba(0,0,0,0.35); backdrop-filter: blur(20px); padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.18); font-size: 12px; }
        .lock-bottom-actions { width: 100%; display: flex; justify-content: space-between; padding: 0 8px; }
        .lock-btn { width: 50px; height: 50px; border-radius: 50%; background: rgba(0,0,0,0.5); backdrop-filter: blur(20px); display: flex; justify-content: center; align-items: center; font-size: 18px; border: 1px solid rgba(255,255,255,0.25); color: white; cursor: pointer; }

        /* FACE ID OVERLAY */
        .faceid-overlay {
            position: absolute; inset: 0; z-index: 150; background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(25px);
            display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 20px;
            opacity: 0; pointer-events: none; transition: opacity 0.3s ease; cursor: pointer;
        }
        .faceid-overlay.active { opacity: 1; pointer-events: auto; }
        .faceid-scanner-frame { 
            width: 180px; height: 180px; border-radius: 50%; position: relative; 
            display: flex; justify-content: center; align-items: center; 
            overflow: hidden; border: 3px solid rgba(255,255,255,0.3); background: #111;
        }
        .faceid-scanner-frame video { width: 100%; height: 100%; object-fit: cover; transform: scaleX(-1); position: absolute; top: 0; left: 0; }
        .faceid-laser { position: absolute; width: 100%; height: 3px; background: linear-gradient(90deg, transparent, #007aff, #34c759, transparent); top: 0; animation: scanLaser 1.5s infinite ease-in-out; z-index: 2; }
        @keyframes scanLaser { 0% { top: 0%; } 50% { top: 100%; } 100% { top: 0%; } }

        /* CENTRO DE CONTROL */
        .control-center-overlay {
            position: absolute; inset: 0; z-index: 90; background: rgba(18, 32, 28, 0.85); backdrop-filter: blur(45px);
            padding: 12px 18px 24px 18px; display: flex; flex-direction: column; gap: 14px;
            transform: translateY(-100%); opacity: 0; pointer-events: none; transition: all 0.38s cubic-bezier(0.16, 1, 0.3, 1); color: white;
        }
        .control-center-overlay.active { transform: translateY(0); opacity: 1; pointer-events: auto; }
        .cc-top-bar { display: flex; justify-content: space-between; align-items: center; margin-top: 36px; }
        .cc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
        .cc-card { background: rgba(255, 255, 255, 0.12); backdrop-filter: blur(30px); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 28px; padding: 12px; }
        .cc-icon-btn { aspect-ratio: 1; border-radius: 50%; background: rgba(255, 255, 255, 0.15); display: flex; justify-content: center; align-items: center; font-size: 18px; color: white; cursor: pointer; }
        .cc-icon-btn.active-blue { background: #007aff; }
        .cc-icon-btn.active-green { background: #34c759; }

        .v-slider-container { height: 130px; background: rgba(255, 255, 255, 0.2); border-radius: 35px; position: relative; overflow: hidden; cursor: pointer; display: flex; flex-direction: column; justify-content: flex-end; }
        .v-slider-fill { width: 100%; background: #ffffff; border-radius: 0 0 35px 35px; }
        .v-slider-icon { position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%); font-size: 20px; color: #1c1c1e; pointer-events: none; z-index: 2; }

        /* PANTALLA DE INICIO (HOME SCREEN) */
        .home-screen { position: absolute; inset: 0; padding: 50px 18px 22px 18px; display: flex; flex-direction: column; justify-content: space-between; z-index: 2; }
        .widgets-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 12px; }
        .widget { height: 135px; border-radius: 24px; padding: 14px; color: white; box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
        .widget-weather { background: linear-gradient(135deg, #1e40af, #3b82f6); display: flex; flex-direction: column; justify-content: space-between; }
        .widget-calendar { background: #ffffff; color: #000; display: flex; flex-direction: column; }

        .app-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px 10px; }
        .app-item { display: flex; flex-direction: column; align-items: center; gap: 4px; cursor: pointer; }
        .app-icon {
            width: 58px; height: 58px; border-radius: var(--ios-radius); display: flex; justify-content: center; align-items: center;
            font-size: 25px; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .app-label { color: white; font-size: 11px; font-weight: 500; text-shadow: 0 1px 3px rgba(0,0,0,0.9); }

        .dock { background: rgba(255, 255, 255, 0.25); backdrop-filter: blur(30px); border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 32px; padding: 10px 12px; display: flex; justify-content: space-between; }

        /* VENTANAS DE APPS */
        .app-window {
            position: absolute; inset: 0; background: #000; z-index: 50;
            transform: scale(0.85) translateY(100%); opacity: 0; pointer-events: none;
            transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
            display: flex; flex-direction: column; padding-top: 48px; color: white; overflow: hidden;
        }
        .app-window.active { transform: scale(1) translateY(0); opacity: 1; pointer-events: auto; }
        .app-header { padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.1); font-weight: 600; font-size: 17px; }

        /* APP: MUSICA */
        .music-player { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: space-around; padding: 20px; }
        .album-art { width: 240px; height: 240px; border-radius: 20px; background: linear-gradient(135deg, #ec4899, #8b5cf6); box-shadow: 0 15px 35px rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; font-size: 70px; }
        .progress-bar-bg { width: 100%; height: 6px; background: #333; border-radius: 3px; cursor: pointer; position: relative; }
        .progress-bar-fill { width: 35%; height: 100%; background: #fff; border-radius: 3px; }

        /* APP: GALERÍA */
        .photos-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px; padding: 4px; flex: 1; overflow-y: auto; }
        .photo-thumb { aspect-ratio: 1; background-size: cover; background-position: center; border-radius: 4px; }

        /* APP: MAPAS */
        #map { width: 100%; flex: 1; z-index: 1; }

        /* APP: RELOJ */
        .clock-tabs { display: flex; border-bottom: 1px solid #222; }
        .clock-tab { flex: 1; padding: 12px; text-align: center; font-size: 14px; color: #888; cursor: pointer; }
        .clock-tab.active { color: #ff9f0a; border-bottom: 2px solid #ff9f0a; font-weight: 600; }
        .timer-display { font-size: 60px; font-weight: 200; text-align: center; margin: 30px 0; }

        /* APP: WHATSAPP */
        .wa-chat-list { display: flex; flex-direction: column; flex: 1; overflow-y: auto; }
        .wa-chat-item { display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-bottom: 1px solid #1f2937; cursor: pointer; }
        .wa-avatar { width: 48px; height: 48px; border-radius: 50%; background: #374151; display: flex; justify-content: center; align-items: center; font-size: 20px; }
        .wa-chat-view { position: absolute; inset: 48px 0 0 0; background: #0b141a; display: flex; flex-direction: column; transform: translateX(100%); transition: transform 0.3s; z-index: 2; }
        .wa-chat-view.open { transform: translateX(0); }
        .wa-messages { flex: 1; padding: 12px; display: flex; flex-direction: column; gap: 8px; overflow-y: auto; }
        .wa-msg { max-width: 75%; padding: 8px 12px; border-radius: 12px; font-size: 14px; line-height: 1.4; }
        .wa-msg.sent { background: #005c4b; align-self: flex-end; }
        .wa-msg.received { background: #202c33; align-self: flex-start; }

        /* APP: CALCULADORA */
        .calc-btn {
            height: 62px; border-radius: 50%; border: none; font-size: 22px; font-weight: 500; color: white; cursor: pointer;
            display: flex; justify-content: center; align-items: center; transition: filter 0.1s;
        }
        .calc-btn:active { filter: brightness(1.3); }
        .calc-btn.gray { background: #a5a5a5; color: black; }
        .calc-btn.dark { background: #333333; }
        .calc-btn.orange { background: #ff9f0a; }

        /* APP: BLOCK BEAST */
        #beastCanvas { background: #111827; display: block; width: 100%; flex: 1; }
        .game-controls { display: flex; justify-content: space-around; padding: 16px; background: #0f172a; border-top: 1px solid #1e293b; }
        .game-btn { width: 70px; height: 50px; background: #3b82f6; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-size: 22px; cursor: pointer; }

        /* APP: AJUSTES */
        .settings-list { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 16px; background: #000; }
        .settings-group { background: #1c1c1e; border-radius: 14px; overflow: hidden; }
        .settings-row { display: flex; justify-content: space-between; align-items: center; padding: 12px 16px; border-bottom: 1px solid #2c2c2e; font-size: 15px; }
        .ios-switch { position: relative; width: 50px; height: 30px; }
        .ios-switch input { opacity: 0; width: 0; height: 0; }
        .switch-slider { position: absolute; inset: 0; background-color: #3a3a3c; border-radius: 30px; transition: .3s; }
        .switch-slider:before { position: absolute; content: ""; height: 26px; width: 26px; left: 2px; bottom: 2px; background-color: white; border-radius: 50%; transition: .3s; }
        input:checked + .switch-slider { background-color: #34c759; }
        input:checked + .switch-slider:before { transform: translateX(20px); }

        /* HOME INDICATOR */
        .home-indicator { position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%); width: 135px; height: 5px; background: #ffffff; border-radius: 3px; z-index: 200; cursor: pointer; }
    </style>
</head>
<body>

<div class="viewport-scaler">
    <div class="iphone-container" id="iphone">

        <!-- Status Bar -->
        <div class="status-bar">
            <span id="clock-time" onclick="toggleNotifCenter()">11:36</span>
            <div class="status-icons" onclick="toggleControlCenter()">
                <i class="fa-solid fa-signal"></i>
                <span>5G</span>
                <i class="fa-solid fa-battery-three-quarters"></i>
            </div>
        </div>

        <!-- Dynamic Island -->
        <div class="dynamic-island" id="island">
            <div id="island-left" style="display:flex; align-items:center; gap:6px;">
                <div id="island-icon" style="width:8px; height:8px; background:#ef4444; border-radius:50%; display:none;"></div>
                <span id="island-text" style="font-size:11px; display:none;">00:00</span>
            </div>
            <div id="island-right" style="display:flex; align-items:center; gap:6px;">
                <div class="eq-bar-container" id="island-eq" style="display:none;">
                    <div class="eq-bar"></div><div class="eq-bar"></div><div class="eq-bar"></div>
                </div>
                <div style="width:10px; height:10px; background:#111; border-radius:50%;"></div>
            </div>
        </div>

        <!-- NOTIFICATION BANNER -->
        <div class="notif-banner" id="notif-banner">
            <i class="fa-solid fa-bell" id="notif-icon" style="font-size:20px; color:#3b82f6;"></i>
            <div style="flex:1;">
                <div style="font-weight:700; font-size:13px;" id="notif-title">Notificación</div>
                <div style="font-size:12px; color:#ccc;" id="notif-body">Mensaje recibido</div>
            </div>
        </div>

        <!-- CENTRO DE NOTIFICACIONES -->
        <div class="notif-center" id="notif-center" onclick="toggleNotifCenter()">
            <div style="font-size:22px; font-weight:700; margin-bottom:10px;">Centro de Notificaciones</div>
            <div id="notif-list" style="display:flex; flex-direction:column; gap:10px;">
                <div style="background:rgba(255,255,255,0.15); padding:12px; border-radius:16px;">
                    <div style="font-weight:600; font-size:13px;">WhatsApp • Hace 5m</div>
                    <div style="font-size:12px; opacity:0.8;">Juan: ¡La suite de iOS 18 quedó genial!</div>
                </div>
            </div>
        </div>

        <!-- PANTALLA DE BLOQUEO -->
        <div class="lock-screen" id="lock-screen" onclick="startFaceIDScan()">
            <div style="text-align:center;">
                <i class="fa-solid fa-lock" id="lock-icon" style="font-size:20px; margin-bottom:8px; opacity:0.8;"></i>
                <div class="lock-date" id="lock-date">Martes, 17 de Octubre</div>
                <div class="lock-clock" id="lock-clock">11:36</div>
                <div class="lock-widgets">
                    <span><i class="fa-solid fa-cloud-sun"></i> 23°</span>
                    <span>•</span>
                    <span><i class="fa-solid fa-heart-pulse" style="color:#ef4444;"></i> 72 BPM</span>
                </div>
            </div>

            <div style="font-size:12px; opacity:0.8; margin-bottom:10px;">Toca para desbloquear</div>

            <div class="lock-bottom-actions">
                <div class="lock-btn" onclick="event.stopPropagation(); triggerNotif('Linterna', 'Modo linterna activado', 'fa-flashlight');"><i class="fa-solid fa-flashlight"></i></div>
                <div class="lock-btn" onclick="event.stopPropagation(); startFaceIDScan();"><i class="fa-solid fa-camera"></i></div>
            </div>
        </div>

        <!-- FACE ID MODAL SCANNER -->
        <div class="faceid-overlay" id="faceid-modal" onclick="forceUnlock()">
            <div class="faceid-scanner-frame">
                <video id="faceid-video" autoplay playsinline muted></video>
                <div class="faceid-laser" id="faceid-laser"></div>
                <i class="fa-solid fa-face-smile" id="faceid-mesh" style="font-size:80px; color:rgba(255,255,255,0.3); z-index:2;"></i>
                <i class="fa-solid fa-circle-check" id="faceid-check" style="font-size:60px; color:#34c759; display:none; z-index:3;"></i>
            </div>
            <div style="color:white; font-size:15px; font-weight:600;" id="faceid-text">Escaneando rostro...</div>
        </div>

        <!-- CENTRO DE CONTROL -->
        <div class="control-center-overlay" id="control-center">
            <div class="cc-top-bar">
                <div class="cc-icon-btn" style="width:36px; height:36px; font-size:14px;"><i class="fa-solid fa-plus"></i></div>
                <div class="cc-icon-btn" style="width:36px; height:36px; font-size:14px;" onclick="lockPhone()"><i class="fa-solid fa-power-off"></i></div>
            </div>

            <div class="cc-grid">
                <div class="cc-card" style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                    <div class="cc-icon-btn active-blue"><i class="fa-solid fa-plane"></i></div>
                    <div class="cc-icon-btn active-blue"><i class="fa-solid fa-satellite-dish"></i></div>
                    <div class="cc-icon-btn active-blue"><i class="fa-solid fa-wifi"></i></div>
                    <div class="cc-icon-btn active-green"><i class="fa-solid fa-tower-cell"></i></div>
                </div>

                <div class="cc-card" style="display:flex; flex-direction:column; justify-content:space-between;">
                    <div style="font-size:13px; font-weight:600;" id="cc-music-title">Starboy</div>
                    <div style="font-size:11px; color:#aaa;" id="cc-music-artist">The Weeknd</div>
                    <div style="display:flex; justify-content:space-around; font-size:18px;">
                        <i class="fa-solid fa-backward-step" onclick="prevTrack()" style="cursor:pointer;"></i>
                        <i class="fa-solid fa-play" id="cc-play-btn" onclick="togglePlayMusic()" style="cursor:pointer;"></i>
                        <i class="fa-solid fa-forward-step" onclick="nextTrack()" style="cursor:pointer;"></i>
                    </div>
                </div>
            </div>

            <div class="cc-grid">
                <div class="v-slider-container">
                    <div class="v-slider-fill" style="height: 70%;"></div>
                    <i class="fa-solid fa-sun v-slider-icon"></i>
                </div>
                <div class="v-slider-container">
                    <div class="v-slider-fill" style="height: 50%;"></div>
                    <i class="fa-solid fa-volume-high v-slider-icon"></i>
                </div>
            </div>
        </div>

        <!-- PANTALLA DE INICIO (HOME SCREEN) -->
        <div class="home-screen">
            <div>
                <div class="widgets-grid">
                    <div class="widget widget-weather">
                        <div style="font-size: 11px; font-weight: 600;">Las Gabias <i class="fa-solid fa-location-arrow" style="font-size:9px;"></i></div>
                        <div>
                            <div style="font-size: 32px; font-weight: 700;">23°</div>
                            <div style="font-size: 11px;">Soleado</div>
                        </div>
                        <div style="font-size: 10px; opacity: 0.85;">Máx. 27° Mín. 15°</div>
                    </div>
                    <div class="widget widget-calendar">
                        <div style="color: #ef4444; font-size: 11px; font-weight: 700;">MARTES</div>
                        <div style="font-size: 36px; font-weight: 800; line-height: 1;">17</div>
                        <div style="margin-top: auto; font-size: 10px; color: #6b7280; font-weight: 500;">Sin eventos</div>
                    </div>
                </div>

                <div class="app-grid">
                    <div class="app-item" onclick="openApp('app-whatsapp')">
                        <div class="app-icon" style="background:#25d366;"><i class="fa-brands fa-whatsapp"></i></div>
                        <span class="app-label">WhatsApp</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-music')">
                        <div class="app-icon" style="background:linear-gradient(135deg, #fa2d48, #fb6470);"><i class="fa-solid fa-music"></i></div>
                        <span class="app-label">Música</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-photos')">
                        <div class="app-icon" style="background:#fff; color:#000;"><i class="fa-solid fa-images" style="color:#f59e0b;"></i></div>
                        <span class="app-label">Fotos</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-maps'); initMap();">
                        <div class="app-icon" style="background:#10b981;"><i class="fa-solid fa-map-location-dot"></i></div>
                        <span class="app-label">Mapas</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-clock')">
                        <div class="app-icon" style="background:#000; border:1px solid #333;"><i class="fa-regular fa-clock"></i></div>
                        <span class="app-label">Reloj</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-camera'); startCamera();">
                        <div class="app-icon" style="background:#4b5563;"><i class="fa-solid fa-camera"></i></div>
                        <span class="app-label">Cámara</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-blockbeast'); initBlockBeast();">
                        <div class="app-icon" style="background:linear-gradient(135deg, #a855f7, #6366f1);"><i class="fa-solid fa-cubes-stacked"></i></div>
                        <span class="app-label">Block Beast</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-settings')">
                        <div class="app-icon" style="background:#6b7280;"><i class="fa-solid fa-gear"></i></div>
                        <span class="app-label">Ajustes</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-notes')">
                        <div class="app-icon" style="background:#eab308;"><i class="fa-solid fa-note-sticky"></i></div>
                        <span class="app-label">Notas</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-mail')">
                        <div class="app-icon" style="background:#3b82f6;"><i class="fa-solid fa-envelope"></i></div>
                        <span class="app-label">Mail</span>
                    </div>

                    <div class="app-item" onclick="openApp('app-calc')">
                        <div class="app-icon" style="background:#333;"><i class="fa-solid fa-calculator"></i></div>
                        <span class="app-label">Calculadora</span>
                    </div>

                    <div class="app-item" onclick="lockPhone()">
                        <div class="app-icon" style="background:#ef4444;"><i class="fa-solid fa-lock"></i></div>
                        <span class="app-label">Bloquear</span>
                    </div>
                </div>
            </div>

            <!-- DOCK -->
            <div class="dock">
                <div class="app-icon" style="background:#22c55e;" onclick="triggerNotif('Teléfono', 'Llamada perdida de Juan', 'fa-phone')"><i class="fa-solid fa-phone"></i></div>
                <div class="app-icon" style="background:#3b82f6;" onclick="openApp('app-maps'); initMap();"><i class="fa-regular fa-compass"></i></div>
                <div class="app-icon" style="background:#0284c7;" onclick="openApp('app-mail')"><i class="fa-solid fa-envelope"></i></div>
                <div class="app-icon" style="background:#25d366;" onclick="openApp('app-whatsapp')"><i class="fa-brands fa-whatsapp"></i></div>
            </div>
        </div>

        <!-- APP: APPLE MUSIC -->
        <div class="app-window" id="app-music">
            <div class="app-header"><span>Apple Music</span></div>
            <div class="music-player">
                <div class="album-art"><i class="fa-solid fa-music"></i></div>
                <div style="text-align:center;">
                    <div style="font-size:20px; font-weight:700;" id="music-title">Starboy</div>
                    <div style="font-size:14px; color:#aaa; margin-top:4px;" id="music-artist">The Weeknd</div>
                </div>
                <div style="width:100%;">
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill" id="music-progress"></div>
                    </div>
                    <div style="display:flex; justify-content:space-between; font-size:11px; color:#aaa; margin-top:6px;">
                        <span>1:15</span>
                        <span>3:50</span>
                    </div>
                </div>
                <div style="display:flex; justify-content:space-around; width:100%; font-size:28px; align-items:center;">
                    <i class="fa-solid fa-backward-step" onclick="prevTrack()" style="cursor:pointer;"></i>
                    <i class="fa-solid fa-circle-play" id="music-main-play" onclick="togglePlayMusic()" style="font-size:54px; color:#fa2d48; cursor:pointer;"></i>
                    <i class="fa-solid fa-forward-step" onclick="nextTrack()" style="cursor:pointer;"></i>
                </div>
            </div>
        </div>

        <!-- APP: FOTOS -->
        <div class="app-window" id="app-photos">
            <div class="app-header"><span>Biblioteca de Fotos</span></div>
            <div class="photos-grid">
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=1');"></div>
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=2');"></div>
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=3');"></div>
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=4');"></div>
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=5');"></div>
                <div class="photo-thumb" style="background-image:url('https://picsum.photos/200/200?random=6');"></div>
            </div>
        </div>

        <!-- APP: MAPAS -->
        <div class="app-window" id="app-maps">
            <div class="app-header"><span>Mapas</span></div>
            <div id="map"></div>
        </div>

        <!-- APP: RELOJ -->
        <div class="app-window" id="app-clock">
            <div class="clock-tabs">
                <div class="clock-tab active" id="tab-sw" onclick="switchClockTab('sw')">Cronómetro</div>
                <div class="clock-tab" id="tab-tm" onclick="switchClockTab('tm')">Temporizador</div>
            </div>
            <div id="clock-sw-view" style="padding:20px; flex:1; display:flex; flex-direction:column; justify-content:space-around;">
                <div class="timer-display" id="sw-display">00:00.0</div>
                <div style="display:flex; justify-content:space-around;">
                    <div class="lock-btn" style="width:70px; height:70px;" onclick="resetStopwatch()">Reset</div>
                    <div class="lock-btn" style="width:70px; height:70px; background:#34c759;" id="sw-start-btn" onclick="toggleStopwatch()">Iniciar</div>
                </div>
            </div>
            <div id="clock-tm-view" style="padding:20px; flex:1; display:none; flex-direction:column; justify-content:space-around;">
                <div class="timer-display" id="tm-display">01:00</div>
                <div style="display:flex; justify-content:space-around;">
                    <div class="lock-btn" style="width:70px; height:70px;" onclick="resetTimer()">Reset</div>
                    <div class="lock-btn" style="width:70px; height:70px; background:#34c759;" id="tm-start-btn" onclick="toggleTimer()">Iniciar</div>
                </div>
            </div>
        </div>

        <!-- APP: CÁMARA -->
        <div class="app-window" id="app-camera">
            <div class="app-header"><span>Cámara</span></div>
            <video id="camera-feed" autoplay playsinline muted style="width:100%; height:100%; object-fit:cover;"></video>
        </div>

        <!-- APP: WHATSAPP -->
        <div class="app-window" id="app-whatsapp">
            <div class="app-header"><span>WhatsApp</span></div>
            <div class="wa-chat-list">
                <div class="wa-chat-item" onclick="openWaChat('Juan Pérez')">
                    <div class="wa-avatar"><i class="fa-solid fa-user"></i></div>
                    <div>
                        <div style="font-weight:600; font-size:15px;">Juan Pérez</div>
                        <div style="font-size:12px; color:#aaa;">¡La suite de iOS 18 quedó genial!</div>
                    </div>
                </div>
            </div>
            <div class="wa-chat-view" id="wa-chat-view">
                <div class="app-header" style="background:#1f2937;">
                    <span onclick="closeWaChat()" style="cursor:pointer;"><i class="fa-solid fa-arrow-left"></i> Atrás</span>
                    <span id="wa-chat-title">Chat</span>
                </div>
                <div class="wa-messages">
                    <div class="wa-msg received">Hola, ¿cómo estás?</div>
                    <div class="wa-msg sent">¡Todo excelente probando iOS 18!</div>
                </div>
            </div>
        </div>

        <!-- APP: BLOCK BEAST -->
        <div class="app-window" id="app-blockbeast">
            <div class="app-header"><span>Block Beast</span></div>
            <canvas id="beastCanvas"></canvas>
            <div class="game-controls">
                <div class="game-btn" onclick="moveBlock(-20)"><i class="fa-solid fa-arrow-left"></i></div>
                <div class="game-btn" onclick="moveBlock(20)"><i class="fa-solid fa-arrow-right"></i></div>
            </div>
        </div>

        <!-- APP: AJUSTES -->
        <div class="app-window" id="app-settings">
            <div class="app-header"><span>Ajustes</span></div>
            <div class="settings-list">
                <div class="settings-group">
                    <div class="settings-row">
                        <span>Modo Oscuro</span>
                        <label class="ios-switch"><input type="checkbox" checked><span class="switch-slider"></span></label>
                    </div>
                    <div class="settings-row">
                        <span>Wi-Fi</span>
                        <span style="color:#aaa;">Activado</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- APP: NOTAS -->
        <div class="app-window" id="app-notes">
            <div class="app-header"><span>Notas</span></div>
            <textarea style="width:100%; flex:1; background:#1c1c1e; color:white; border:none; padding:16px; font-size:16px; outline:none; resize:none;" placeholder="Escribe aquí tu nota..."></textarea>
        </div>

        <!-- APP: MAIL -->
        <div class="app-window" id="app-mail">
            <div class="app-header"><span>Buzón</span></div>
            <div style="padding:16px; color:#aaa;">No hay correos nuevos.</div>
        </div>

        <!-- APP: CALCULADORA -->
        <div class="app-window" id="app-calc">
            <div class="app-header"><span>Calculadora</span></div>
            <div style="flex:1; display:flex; flex-direction:column; justify-content:flex-end; padding:20px;">
                <div style="font-size:48px; text-align:right; margin-bottom:20px; font-weight:300;" id="calc-display">0</div>
                <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:10px;">
                    <button class="calc-btn gray" onclick="calcInput('C')">C</button>
                    <button class="calc-btn gray" onclick="calcInput('/')">/</button>
                    <button class="calc-btn gray" onclick="calcInput('*')">*</button>
                    <button class="calc-btn orange" onclick="calcInput('-')">-</button>
                    <button class="calc-btn dark" onclick="calcInput('7')">7</button>
                    <button class="calc-btn dark" onclick="calcInput('8')">8</button>
                    <button class="calc-btn dark" onclick="calcInput('9')">9</button>
                    <button class="calc-btn orange" onclick="calcInput('+')">+</button>
                    <button class="calc-btn dark" onclick="calcInput('4')">4</button>
                    <button class="calc-btn dark" onclick="calcInput('5')">5</button>
                    <button class="calc-btn dark" onclick="calcInput('6')">6</button>
                    <button class="calc-btn orange" onclick="calcEval()">=</button>
                    <button class="calc-btn dark" onclick="calcInput('1')">1</button>
                    <button class="calc-btn dark" onclick="calcInput('2')">2</button>
                    <button class="calc-btn dark" onclick="calcInput('3')">3</button>
                    <button class="calc-btn dark" onclick="calcInput('0')">0</button>
                </div>
            </div>
        </div>

        <!-- HOME INDICATOR -->
        <div class="home-indicator" onclick="closeCurrentApp()"></div>

    </div>
</div>

<script>
    // RELOJ PANTALLA
    function updateClocks() {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const timeStr = `${hours}:${minutes}`;
        document.getElementById('clock-time').innerText = timeStr;
        document.getElementById('lock-clock').innerText = timeStr;
    }
    setInterval(updateClocks, 1000);
    updateClocks();

    // CENTROS DE CONTROL Y NOTIFICACIONES
    function toggleNotifCenter() { document.getElementById('notif-center').classList.toggle('active'); }
    function toggleControlCenter() { document.getElementById('control-center').classList.toggle('active'); }

    // ABRIR / CERRAR APPS
    function openApp(id) {
        document.querySelectorAll('.app-window').forEach(app => app.classList.remove('active'));
        const target = document.getElementById(id);
        if(target) target.classList.add('active');
    }
    function closeCurrentApp() {
        document.querySelectorAll('.app-window').forEach(app => app.classList.remove('active'));
    }

    // BLOQUEO & FACE ID
    function lockPhone() {
        document.getElementById('control-center').classList.remove('active');
        document.getElementById('lock-screen').classList.remove('unlocked');
        closeCurrentApp();
    }

    let scanTimer = null;
    let cameraStream = null;

    function forceUnlock() {
        if (scanTimer) clearTimeout(scanTimer);
        const modal = document.getElementById('faceid-modal');
        modal.classList.remove('active');
        document.getElementById('lock-screen').classList.add('unlocked');
        if (cameraStream) {
            cameraStream.getTracks().forEach(t => t.stop());
            cameraStream = null;
        }
    }

    function startFaceIDScan() {
        const modal = document.getElementById('faceid-modal');
        const video = document.getElementById('faceid-video');
        const text = document.getElementById('faceid-text');
        const check = document.getElementById('faceid-check');
        const mesh = document.getElementById('faceid-mesh');

        modal.classList.add('active');
        text.innerText = "Escaneando rostro...";
        check.style.display = "none";
        mesh.style.display = "block";

        let isDone = false;
        function completeScan() {
            if (isDone) return;
            isDone = true;
            check.style.display = "block";
            mesh.style.display = "none";
            text.innerText = "Rostro reconocido";
            setTimeout(forceUnlock, 500);
        }

        scanTimer = setTimeout(completeScan, 900);

        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .then(stream => { cameraStream = stream; video.srcObject = stream; })
                .catch(() => {});
        }
    }

    // CALCULADORA
    let calcVal = "";
    function calcInput(v) {
        if (v === 'C') calcVal = "";
        else calcVal += v;
        document.getElementById('calc-display').innerText = calcVal || "0";
    }
    function calcEval() {
        try {
            calcVal = String(eval(calcVal));
            document.getElementById('calc-display').innerText = calcVal;
        } catch {
            document.getElementById('calc-display').innerText = "Error";
            calcVal = "";
        }
    }

    // MUSICA
    let isPlaying = false;
    function togglePlayMusic() {
        isPlaying = !isPlaying;
        document.getElementById('music-main-play').className = isPlaying ? "fa-solid fa-circle-pause" : "fa-solid fa-circle-play";
        document.getElementById('cc-play-btn').className = isPlaying ? "fa-solid fa-pause" : "fa-solid fa-play";
    }
    function nextTrack() { triggerNotif('Música', 'Siguiente pista', 'fa-music'); }
    function prevTrack() { triggerNotif('Música', 'Pista anterior', 'fa-music'); }

    // RELOJ & CRONOMETRO
    function switchClockTab(tab) {
        document.getElementById('tab-sw').classList.toggle('active', tab === 'sw');
        document.getElementById('tab-tm').classList.toggle('active', tab === 'tm');
        document.getElementById('clock-sw-view').style.display = tab === 'sw' ? 'flex' : 'none';
        document.getElementById('clock-tm-view').style.display = tab === 'tm' ? 'flex' : 'none';
    }

    let swInterval = null, swSec = 0;
    function toggleStopwatch() {
        const btn = document.getElementById('sw-start-btn');
        if (swInterval) {
            clearInterval(swInterval);
            swInterval = null;
            btn.innerText = "Iniciar";
        } else {
            swInterval = setInterval(() => {
                swSec += 0.1;
                document.getElementById('sw-display').innerText = swSec.toFixed(1) + 's';
            }, 100);
            btn.innerText = "Pausar";
        }
    }
    function resetStopwatch() {
        clearInterval(swInterval); swInterval = null; swSec = 0;
        document.getElementById('sw-display').innerText = "00:00.0";
        document.getElementById('sw-start-btn').innerText = "Iniciar";
    }

    let tmInterval = null, tmSec = 60;
    function toggleTimer() {
        const btn = document.getElementById('tm-start-btn');
        if (tmInterval) {
            clearInterval(tmInterval); tmInterval = null; btn.innerText = "Iniciar";
        } else {
            tmInterval = setInterval(() => {
                if (tmSec > 0) {
                    tmSec--;
                    document.getElementById('tm-display').innerText = `00:${String(tmSec).padStart(2, '0')}`;
                } else {
                    clearInterval(tmInterval); tmInterval = null; alert("¡Tiempo finalizado!");
                }
            }, 1000);
            btn.innerText = "Pausar";
        }
    }
    function resetTimer() {
        clearInterval(tmInterval); tmInterval = null; tmSec = 60;
        document.getElementById('tm-display').innerText = "01:00";
        document.getElementById('tm-start-btn').innerText = "Iniciar";
    }

    // MAPAS
    let map = null;
    function initMap() {
        if (!map) {
            setTimeout(() => {
                map = L.map('map').setView([37.15, -3.65], 13);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
            }, 200);
        }
    }

    // WHATSAPP
    function openWaChat(name) {
        document.getElementById('wa-chat-title').innerText = name;
        document.getElementById('wa-chat-view').classList.add('open');
    }
    function closeWaChat() { document.getElementById('wa-chat-view').classList.remove('open'); }

    // CÁMARA
    function startCamera() {
        const video = document.getElementById('camera-feed');
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(s => video.srcObject = s)
            .catch(e => console.log(e));
    }

    // BLOCK BEAST
    let bx = 100;
    function initBlockBeast() {
        const canvas = document.getElementById('beastCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight - 80;
        function render() {
            ctx.clearRect(0,0,canvas.width,canvas.height);
            ctx.fillStyle = "#3b82f6";
            ctx.fillRect(bx, canvas.height - 40, 50, 20);
            requestAnimationFrame(render);
        }
        render();
    }
    function moveBlock(dir) { bx += dir; }

    // NOTIFICACIONES BANNER
    function triggerNotif(title, body, icon) {
        const b = document.getElementById('notif-banner');
        document.getElementById('notif-title').innerText = title;
        document.getElementById('notif-body').innerText = body;
        b.classList.add('active');
        setTimeout(() => b.classList.remove('active'), 3000);
    }
</script>
</body>
</html>
"""

if __name__ == '__main__':
    window = webview.create_window('iOS 18 Pro Max Suite', html=HTML_CONTENT, width=450, height=900, resizable=True)
    webview.start()