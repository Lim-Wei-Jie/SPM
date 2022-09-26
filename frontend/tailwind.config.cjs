/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./staff/**/*.{vue,js,ts,jsx,tsx,html}",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}
