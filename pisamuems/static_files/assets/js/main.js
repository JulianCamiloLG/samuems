
$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    $('#cargar').on('click', function(){
    ajaxStart: function start(){
        $("body").addClass("loading")
    }
    ajaxStop: function stop(){
        $("body").removeClass("loading")
    }
 })
});


