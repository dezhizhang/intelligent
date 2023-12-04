/*
 * :file description: 
 * :name: /intelligent/tailwind.config.js
 * :author: 张德志
 * :copyright: (c) 2023, Tungee
 * :date created: 2023-10-07 19:42:34
 * :last editor: 张德志
 * :date last edited: 2023-12-04 20:44:31
 */
import {nextui} from "@nextui-org/react";

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [nextui()],
};