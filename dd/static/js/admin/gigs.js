$(document).ready(function() {
    if ($(".admin.gigs").length) {
        $(".gig .delete").click(function() {
            var gig = $(this).parents(".gig");
            var gid = gig.find("input[name=gid]").val();
            var name = gig.find("input.name").val();
            var confirm = window.prompt("Are you sure you want to delete " + name + "?\nType " + name + " into the box below to confirm.");
            if (name === confirm) {
                var form = gig.find("form");
                var action = form.data("delete");
                form.attr("action", action);
                return true;
            }
            return false;
        });
    }
});