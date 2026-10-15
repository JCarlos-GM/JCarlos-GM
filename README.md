<div align="center">

<img src="./assets/hero.svg" width="100%" alt="Juan Carlos Govea Magaña — Full Stack, IoT, Firmware"/>

<br/>

<a href="https://nexaqua.com.mx"><img src="https://img.shields.io/badge/NexAquA-en_producción-e3262e?style=flat-square&labelColor=0a0a0a"/></a>
<a href="https://polenshoes.com"><img src="https://img.shields.io/badge/Polen-finalizado-3a3a3a?style=flat-square&labelColor=0a0a0a"/></a>
<a href="https://ressly.com.mx"><img src="https://img.shields.io/badge/Ressly-finalizado-3a3a3a?style=flat-square&labelColor=0a0a0a"/></a>
<img src="https://img.shields.io/badge/InnovaTecNM-etapa_nacional-3a3a3a?style=flat-square&labelColor=0a0a0a"/>
<img src="https://komarev.com/ghpvc/?username=JCarlos-GM&style=flat-square&color=3a3a3a&label=visitas"/>

</div>

## Sobre mí

Estudio Ingeniería en Sistemas Computacionales en el TecNM La Piedad. Trabajo en todas las capas de un sistema: diseño la PCB, escribo el firmware y construyo la API, el dashboard, la app móvil y el asistente de voz que los conecta.

Ahora mismo estoy dedicado a **NexAquA**, que está en producción y compite en la etapa nacional de InnovaTecNM. Antes entregué **Polen** y **Ressly**, ambos terminados.

## NexAquA

Sistema IoT de monitoreo hídrico para MiPyMEs agroindustriales. Si un nodo detecta una fuga, la *Defensa Activa* cierra la válvula en menos de 250 ms sin depender de la nube.

<img src="./assets/nexaqua-flow.svg" width="100%" alt="Flujo de datos de NexAquA: sensores, nodos ESP32, broker MQTT, API REST, alertas, HMI Raspberry Pi, ARIA, Dashboard y App Android"/>

| | Repositorio | Qué hace | Stack |
|:-:|:--|:--|:--|
| <img src="https://cdn.simpleicons.org/espressif/8c8c8c" width="18"/> | [Firmware ESP32](https://github.com/JCarlos-GM/NexAquA-ESP32-Firmware) | Nodos maestro/esclavo con pantalla TFT, ESP-NOW, MQTT/TLS y Defensa Activa | C++ · FreeRTOS · LVGL |
| <img src="https://cdn.simpleicons.org/raspberrypi/8c8c8c" width="18"/> | [HMI Raspberry Pi](https://github.com/JCarlos-GM/NexAquA-RPi) | Terminal táctil de operador con control por gestos y voz | React 19 · TypeScript · MediaPipe |
| <img src="https://cdn.simpleicons.org/nodedotjs/8c8c8c" width="18"/> | [API REST](https://github.com/JCarlos-GM/NexAquA-API) | Nodos, eventos, reportes PDF, notificaciones y chatbot con *tool-calling* | Node · Express · Supabase |
| <img src="https://cdn.simpleicons.org/react/8c8c8c" width="18"/> | [Dashboard](https://github.com/JCarlos-GM/NexAquA-Dashboard) | Panel de gerencia: widgets, mapas, ROI y exportación PDF/Excel | React · shadcn/ui · Recharts |
| <img src="https://cdn.simpleicons.org/android/8c8c8c" width="18"/> | [App Android](https://github.com/JCarlos-GM/NexAquA-Android-App) | Operación en campo: alertas, calibración y aprovisionamiento por QR | Java · Retrofit · Firebase |
| <img src="https://cdn.simpleicons.org/python/8c8c8c" width="18"/> | [ARIA](https://github.com/JCarlos-GM/NexAquA-ARIA) | Asistente de voz con el contexto de la empresa, procesamiento local | Python · faster-whisper · Ollama |

## Proyectos entregados

<p align="center">
  <a href="https://polenshoes.com"><img src="./assets/card-polen.svg" width="49%" alt="Polen — ecommerce de sneakers en Guatemala"/></a>
  <a href="https://ressly.com.mx"><img src="./assets/card-ressly.svg" width="49%" alt="Ressly — gestión residencial"/></a>
</p>

## Otros proyectos

| | Proyecto | Descripción | Stack |
|:-:|:--|:--|:--|
| <img src="https://cdn.simpleicons.org/threedotjs/8c8c8c" width="18"/> | [3D Visualizer](https://github.com/JCarlos-GM/NexAquA-3D-Visualizer) | Gemelo digital del invernadero de NexAquA con *GPU instancing* | React Three Fiber · Blender |
| <img src="https://cdn.simpleicons.org/mqtt/8c8c8c" width="18"/> | [nexaqua-bridge](https://github.com/JCarlos-GM/nexaqua-bridge) | Puente MQTT → Firebase Cloud Messaging para alertas push | Node · HiveMQ · FCM |
| <img src="https://cdn.simpleicons.org/typescript/8c8c8c" width="18"/> | [FluxSolver](https://flux-solver.vercel.app) | Jacobi y Gauss-Seidel con entrada por voz, OCR y vista 3D | TypeScript · Tesseract.js |
| <img src="https://cdn.simpleicons.org/react/8c8c8c" width="18"/> | [PseudoHub](https://pseudo-hub.vercel.app) | Generación y validación estadística de números pseudoaleatorios | React 19 · Vite |
| <img src="https://cdn.simpleicons.org/typescript/8c8c8c" width="18"/> | [RegexID](https://regex-id.vercel.app) | Validación en tiempo real de nombre, teléfono, correo, RFC y CURP | TypeScript |
| <img src="https://cdn.simpleicons.org/openjdk/8c8c8c" width="18"/> | [AsmBuilder](https://github.com/JCarlos-GM/AsmBuilder) | CLI que genera plantillas `.asm` para TASM/DOS | Java · Maven |
| <img src="https://cdn.simpleicons.org/python/8c8c8c" width="18"/> | [MathRoots](https://github.com/JCarlos-GM/mathroots) | Bisección y Newton-Raphson con gráficas, voz e imagen | Python |

## Stack

<img src="./assets/stack.svg" width="100%" alt="Stack por capas: IA y voz, interfaces, despliegue, backend y datos, comunicación, firmware y hardware"/>

## Actividad

<p align="center">
  <img src="https://streak-stats.demolab.com?user=JCarlos-GM&background=0A0A0A&border=242424&stroke=242424&ring=E3262E&fire=E3262E&currStreakNum=F5F5F5&sideNums=F5F5F5&currStreakLabel=E3262E&sideLabels=8C8C8C&dates=5C5C5C&border_radius=10&hide_total_contributions=true&locale=es" height="195" alt="Racha de contribuciones"/>
  <img src="./assets/langs.svg" height="195" alt="Lenguajes más usados, repos públicos y privados"/>
</p>

<img src="https://raw.githubusercontent.com/JCarlos-GM/JCarlos-GM/output/github-contribution-grid-snake-red.svg" width="100%" alt="Snake de contribuciones"/>

## Contacto

<a href="mailto:jgoveamagana@gmail.com"><img src="https://img.shields.io/badge/jgoveamagana@gmail.com-0a0a0a?style=for-the-badge&logo=gmail&logoColor=e3262e"/></a>
<a href="https://instagram.com/jcarlosgm2"><img src="https://img.shields.io/badge/@jcarlosgm2-0a0a0a?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://nexaqua.com.mx"><img src="https://img.shields.io/badge/nexaqua.com.mx-0a0a0a?style=for-the-badge&logoColor=white"/></a>
