$(document).ready(function() {
    $(".thenet span").click(function(e) {
        if (e.shiftKey && (e.ctrlKey || e.metaKey)) {
            window.location.href = "/admin/";
        }
    });
});