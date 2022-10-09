/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./staff/**/*.{vue,js,ts,jsx,tsx,html}",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./managerJobRole.html",
    "./jobRoleDetails.html"
  ],
  theme: {
    extend: {},
    container: {
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
  },
  plugins: [require("daisyui")],
}
