/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'class',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {

            backgroundImage: theme => ({
                'custom-image': "url('/static/images/crm.png')",
                'animated-bg': "url('/static/images/bg7.svg')",
                'custom-bg1': "url('/static/images/bg6.svg')",
            }),

            fontFamily: {
                'header': ['Lato-Black', 'sans-serif'],
                'italic': ['italic'],
                'body': ['Lato', 'sans-serif'],
            },

            colors: {
                PRIMARY: 'rgba(22, 25, 34, 1)',
                PRIMARY1: 'rgba(51, 51, 51, 1)',
                SECONDARY1: 'rgba(245, 245, 245, 1)',
                SECONDARY: 'rgba(218, 218, 218, 1)',
                DARK_THEME: {
                    PRIMARY: 'rgba(245, 245, 245, 1)',
                    SECONDARY: 'rgba(12, 25, 44, 1)',
                },
                BLUE1: 'rgba(255, 85, 0, 1)',
                BLUE2: 'rgba(255, 85, 0, 0.83)',
                GREEN1: 'rgba(0, 255, 85, 1)',
                YELLOW_COLOR: 'rgb(247, 88, 14)',
                DARK_MODE1: 'rgba(25, 29, 40, 1)',
                DARK_MODE_CARD: 'rgba(22, 25, 34, 1)',
                DARK_MODE: 'rgba(33, 33, 33, 1)',
                LIGHT_MODE: 'rgba(255, 255, 255, 1)',
                TEXT_COLOR_IN_DM: 'rgba(245, 245, 245, 1)',
                GRAY_GLASS: 'hsla(0, 0%, 55%, 0.178)',
                HEADER_COLOR: 'whitesmoke',
                GRAY_COLOR: 'rgba(63, 66, 68, 1)',
                WHITE_COLOR: 'rgba(255, 255, 255, 1)',
                GLASS: 'rgba(255, 255, 255, 0.1)',
                GLASS_BORDER: 'rgba(255, 255, 255, 0.2)',
                HOVER_COLOR: 'hsla(197, 100%, 51%, 1)',
                DARK_COLOR: 'rgba(0, 0, 0, 1)',
            },
        },
    },
    variants: {},

    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
