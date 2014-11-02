var dd = {
    template_error: _.template("<li class='wrapper error'><%= message %><a class='close' href='javascript:void(0)'><i class='fa fa-times fa-fw'></i></a></li>"),
    error: function(message) {
        $("#messages").append(dd.template_error({message: message}));
    }
};

$(document).ready(function() {
    $("#messages").on("click", "a.close", function() {
        $(this).parents("li").remove();
    });
});
