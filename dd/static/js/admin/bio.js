$(document).ready(function() {
    if ($(".admin.bio").length) {
        $(".bio .delete").click(function() {
            var bio = $(this).parents(".bio");
            var name = bio.find("input.name").val();
            var confirm = window.prompt("Are you sure you want to delete " + name + "?\nType " + name + " into the box below to confirm.");
            if (name === confirm) {
                var form = bio.find("form");
                var action = form.data("delete");
                form.attr("action", action);
                return true;
            }
            return false;
        });
    }
});