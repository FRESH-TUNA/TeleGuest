var headerComponent = {
    template: 
    `
    <div v-bind:class="classObject" v-bind:style="styleObject">
        <div class="container">
        <p></p>
        </div>
    </div>
    `,
    data: function() {
        return {
                classObject: [
                    'jumbotron',
                    'jumbotron-fluid'
                ],
                styleObject:  {
                     height:'700px',
                    'background-image': "url('https://github.com/ros008/test01/blob/master/test/idol.png?raw=true')"
                }
        };
    }
};


var teleguestHeader = new Vue({
    delimiters: ["[[","]]"],
    el: '#header',
    data: {
        
    },
    components: {
        'teleguest-header': headerComponent
    }
});

