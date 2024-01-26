/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/templates/**/*.html', "./node_modules/flowbite/**/*.js", './src/static/js/*.js'],
  theme: {
    extend: {
      spacing:{
        '1/2':'50%',
        '2/3':'66.666667%'
      },
    },
  },
  plugins: [],
}

