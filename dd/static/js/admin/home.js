$(document).ready(function() {
    if ($(".admin.home").length) {
        var validate_user = function(user, skip_password) {
            if (!user.username) {
                dd.error("Missing username");
                return false;
            }
            if (!user.email) {
                dd.error("Missing email");
                return false;
            }
            if (!user.password && !skip_password) {
                dd.error("Missing password");
                return false;
            }
            return true;
        };

        $(".users .edit").click(function() {
            $(this).parents("tr").addClass("editing");
            return false;
        });
        $(".users .save").click(function() {
            var tr = $(this).parents("tr");
            var uid = tr.data("id");
            var data = {
                username: tr.find(".username input").val(),
                email: tr.find(".email input").val(),
                password: tr.find(".password input").val()
            };
            if (validate_user(data, true)) {
                $.ajax({
                    type: "POST",
                    url: "/admin/users/" + uid + "/",
                    data: JSON.stringify(data),
                    contentType : "application/json",
                }).done(function(data, textStatus, jqXHR) {
                    window.location.href = window.location.href;
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    var error = "There was an error, sorry.";
                    try {
                        var r = jqXHR.responseJSON;
                        error = r.error;
                    } finally {
                        dd.error(error);
                    }
                });
            }
            return false;
        });
        $(".users .delete").click(function() {
            var tr = $(this).parents("tr");
            var uid = tr.data("id");
            var username = tr.find(".username input").val();
            var confirm = window.prompt("Are you sure you want to delete " + username + "?\nType " + username + " into the box below to confirm.");
            if (username === confirm) {
                $.ajax({
                    type: "POST",
                    url: "/admin/users/" + uid + "/delete/",
                    data: JSON.stringify({username: confirm}),
                    contentType : "application/json",
                }).done(function(data, textStatus, jqXHR) {
                    window.location.href = window.location.href;
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    var error = "There was an error, sorry.";
                    try {
                        var r = jqXHR.responseJSON;
                        error = r.error;
                    } finally {
                        dd.error(error);
                    }
                });
            }
            return false;
        });
        $(".users a.new").click(function() {
            var tr = $(this).parents("tr");
            var data = {
                username: tr.find(".username input").val(),
                email: tr.find(".email input").val(),
                password: tr.find(".password input").val()
            };
            if (validate_user(data)) {
                $.ajax({
                    type: "POST",
                    url: "/admin/users/",
                    data: JSON.stringify(data),
                    contentType : "application/json",
                }).done(function(data, textStatus, jqXHR) {
                    window.location.href = window.location.href;
                }).fail(function(jqXHR, textStatus, errorThrown) {
                    var error = "There was an error, sorry.";
                    try {
                        var r = jqXHR.responseJSON;
                        error = r.error;
                    } finally {
                        dd.error(error);
                    }
                });
            }
            return false;
        });
    }
});