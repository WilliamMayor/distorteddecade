$(document).ready(function() {
    if ($(".admin.home").length) {
        $(".users .delete").click(function() {
            var user = $(this).parents(".user");
            var uid = user.find("input[name=uid]").val();
            var username = user.find(".username input").val();
            var confirm = window.prompt("Are you sure you want to delete " + username + "?\nType " + username + " into the box below to confirm.");
            if (username === confirm) {
                var form = user.find("form");
                var action = form.data("delete");
                form.attr("action", action);
                return true;
            }
            return false;
        });
    }
});