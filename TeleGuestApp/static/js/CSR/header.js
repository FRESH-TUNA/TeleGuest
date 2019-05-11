var headerComponent = {
    template: 
    `
    <div v-bind:class="classObject" v-bind:style="styleObject">
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

var headerTitleComponent = {
    template:
    `
     <section id="header-title" style="text-align:center;">
            <h1 class="display-4"><strong>Guest House</strong></h1>
            <p class="lead">팬들끼리 소통할 수 있는 공간.</p>
     </section>
    `
};
   

var teleguestHeader = new Vue({
    delimiters: ["[[","]]"],
    el: '#header',
    data: {
        
    },
    components: {
        'teleguest-header': headerComponent,
         'teleguest-header-title': headerTitleComponent
    }
});

