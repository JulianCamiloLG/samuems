$(function () {
  var cargarForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-profesor").modal("show");
      },
      success: function (data) {
        $("#modal-profesor .modal-content").html(data.html_form);
      }
    });
  };

  var guardarForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#tabla-profesores tbody").html(data.html_profesor_list);
          $("#modal-profesor").modal("hide");
        }
        else {
          $("#modal-profesor .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

   // Crear profesor
  $(".js-crear-profesor").click(cargarForm);
  $("#modal-profesor").on("submit", ".js-profe-create-form", guardarForm);

  // Update profesor
  $("#tabla-profesores").on("click", ".js-update-profesor", cargarForm);
  $("#modal-profesor").on("submit", ".js-profe-update-form", guardarForm);

  //Delete profesor
  $("#tabla-profesores").on("click", ".js-delete-profesor", cargarForm);
  $("#modal-profesor").on("submit", ".js-profe-delete-form", guardarForm);

});

