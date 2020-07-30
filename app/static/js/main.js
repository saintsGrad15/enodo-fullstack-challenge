new Vue({
    el: '#app',

    data: {
        searchString: "",
        selectedProperties: []
    },

    methods: {
        search(queryString, callback)
        {
            /**
             * Conduct a substring query of the database on the "Full Address" and
             * "CLASS_DESCRIPTION" fields using the 'queryString.'
             *
             * :param: queryString (str): The substring to use to search the DB.
             *
             * :param: callback (function): The function to call with the results of the query.
             *
             * :return: None
             */

            $.getJSON(`/search/${queryString}/`)
                .then((response) =>
                {
                    const output = [];

                    for (const property of response)
                    {
                        output.push({
                            value: property["Full Address"],
                            index: property["index"]
                        });
                    }

                    callback(output);
                });

        },

        selectProperty({index})
        {
            /**
             * Select property with index 'index.'
             *
             * When finished, clear the search string and
             * refresh the list of selected properties.
             *
             * :param: index (int): The 0-based index the property to select.
             *
             * :return: None
             */

            $.post(`/select_property/${index}/`)
                .then(() => this.refreshSelectedProperties());

            this.searchString = "";
        },

        deselectProperty(index)
        {
            /**
             * Deselect property with index 'index.'
             *
             * When finished, refresh the list of selected properties.
             *
             * :param: index (int): The 0-based index the property to deselect.
             *
             * :return: None
             */

            $.post(`/deselect_property/${index}/`)
                .then(() => this.refreshSelectedProperties());
        },

        refreshSelectedProperties()
        {
            /**
             * Retrieve the list of selected properties and update application state.
             *
             * :return: None
             */

            $.getJSON("/selected/")
                .then((response) =>
                {
                    this.selectedProperties = response;
                })
        }
    },

    created()
    {
        /**
         * Call me when the application is created.
         *
         * Refresh the applications' selected properties state.
         *
         * :return: None
         */

        this.refreshSelectedProperties();
    }
});