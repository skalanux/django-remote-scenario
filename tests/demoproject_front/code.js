(function(exports) {
    'use strict';

    function Questions(name) {
        this.name = name || 'defaultname';
    }
    exports.Questions = Questions;

    Questions.prototype = {
        fetch: function() {
            return $.getJSON('http://localhost:8000/demoapp');
        }
    };
})(this);