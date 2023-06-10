
# LUCAS 2022

Hello nice people!
I made this project to summarize my elaborations with QGIS for the Eurostat LUCAS 2022 project.

You will find my workflow for the development of a dedicated map for the specific needs of a
✨LUCAS Detector Technician✨

There will be explanations accompanied by:
. Slider pictures
. Link videos
. Chart
. Python code for process iteration

I hope you have a good browsing experience and the layout is responsive to your device.

# 🚩 Initialize a Vuejs project
## commit: setting Vue Project

1. after cloning the repo open the terminal from VSC and type: npm create vite@latest . -- --template vue

2. to view always from the terminal: npm i && npm run dev

3. delete the style.css file

4. edit the main.js file: FROM import './style.css' TO import './assets/scss/app.scss'

5. in the 'src' folder --> create 'assets' folder --> create app.scss file

6. Install the SASS package from the terminal: npm add -D sass

7. install Bootstrap: npm i bootstrap @popperjs/core (@popperjs/core these are two libraries that allow you to use Bootstrap 100%)

## Other installations:
npm i vue-chartjs chart.js
# commit
main: add FourthStep, PyAddData, SliderCsvPivot, install [ npm i vue-chartjs chart.js ] to add charts


# Vue 3 + Vite

This template should help get you started developing with Vue 3 in Vite. The template uses Vue 3 `<script setup>` SFCs, check out the [script setup docs](https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup) to learn more.

## Recommended IDE Setup

- [VS Code](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

