$(document).ready(function() {
    if ($(".admin.music").length) {
        $(".embed .delete").click(function() {
            var embed = $(this).parents(".embed");
            var name = embed.find("input.name").val();
            var confirm = window.prompt("Are you sure you want to delete " + name + "?\nType " + name + " into the box below to confirm.");
            if (name === confirm) {
                var form = embed.find("form");
                var action = form.data("delete");
                form.attr("action", action);
                return true;
            }
            return false;
        });
    }
});