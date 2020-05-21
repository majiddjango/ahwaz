// A $( document ).ready() block.
$( document ).ready(function() {
// ---------------------------------------------------

    $('#replymodal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var recipient = button.data('id'); // Extract info from data-* attributes
    $('#cid').val(recipient);
    });

    $( "#search_col" ).mouseover(function() {
        $('#search_results').show();
      });
      $( "#search_col" ).mouseout(function() {
        $('#search_results').hide();
      });

    $("#search").keyup(function() {
        if($(this).val().length >= 3) {

            console.log($(this).val());

            var form = $('#search_form');
            var url = form.attr('action');
        
            $.ajax({
                   type: "GET",
                   url: url,
                   data: form.serialize(), // serializes the form's elements.
                   success: function(data)
                   {
                       $('#search_results').html(data);
                    console.log(data); // show response from the php script.
                   }
                 });
            

             // Enable submit button
        } else {
             // Disable submit button
        }
    });
    

});

