/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html", "index.html"],
  darkMode: "class",
  theme: {
    extend: {
      typography: ({ theme }) => ({
        "neutral-dark": {
          css: {
            "--tw-prose-body": theme("colors.neutral.100"),
            "--tw-prose-headings": theme("colors.white"),
            "--tw-prose-pre-bg": theme("colors.neutral.800"),
            "--tw-prose-links": theme("colors.blue[600]"),
            "--tw-prose-bold": theme("colors.cyan[300]"),
            backgroundColor: theme("colors.neutral.900"),
          },
        },
      }),
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
