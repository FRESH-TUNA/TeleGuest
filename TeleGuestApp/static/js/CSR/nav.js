Vue.component('navapp', {
    delimiters: ["[[","]]"],
    props: ['title'],
    template:
    `
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">[[title]]</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">

            </ul>
            <form class="form-inline my-2 my-lg-0" action="/#">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" id='kw1' name='kw2'>
                <button class="btn btn-outline-dark my-2 my-sm-0" type="submit">검색</button>
            </form>
        </div>
    </nav>
    `
})
var navVue = new Vue({
    delimiters: ["[[","]]"],
    el: '#nav',
    data: {
        title: 'TeleGuest'
    }
});