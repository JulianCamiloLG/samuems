$(function () {
  var cargarFormMaterias = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-materia").modal("show");
      },
      success: function (data) {
        $("#modal-materia .modal-content").html(data.html_form);
      }
    });
  };

  var guardarFormMaterias = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#tabla-materias tbody").html(data.html_materia_list);
          $("#modal-materia").modal("hide");
        }
        else {
          $("#modal-materia .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

   // Crear Materia
  $(".js-crear-materia").click(cargarFormMaterias);
  $("#modal-materia").on("submit", ".js-materia-create-form", guardarFormMaterias);

  // Update Materia
  $("#tabla-materias").on("click", ".js-update-materia", cargarFormMaterias);
  $("#modal-materia").on("submit", ".js-materia-update-form", guardarFormMaterias);

  //Delete Materia
  $("#tabla-materias").on("click", ".js-delete-materia", cargarFormMaterias);
  $("#modal-materia").on("submit", ".js-materia-delete-form", guardarFormMaterias);

});

