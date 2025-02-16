/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Enables manual dark mode toggling
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",  // Ensures Tailwind scans your Vue components
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
