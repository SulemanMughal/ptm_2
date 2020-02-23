
            setInterval(function sharelist1(){
                var a = document.getElementById('listid').value;
                document.getElementById('listname').innerHTML = document.getElementById(a).value;
            },500);
            function sharelist(a){
                var b = document.getElementById('listid').value;
                var h = new XMLHttpRequest();
                h.open("GET","/share-list/"+a.value+"/"+b);
                h.send()
                alert('List has been shared with '+a.value);
                a.value = '';
            }
            function sharelistb(a){
                var b = document.getElementById('listid').value;
                var h = new XMLHttpRequest();
                h.open("GET","/share-list-buyer/"+a.value+"/"+b);
                h.send()
                alert('List has been shared with '+a.value);
                a.value = '';
            }
            function removefunc(){
                var a = document.getElementById('listid').value;
                var h = new XMLHttpRequest();
                h.open("GET","/unlink/"+a);
                h.send();
                alert('List has been unlinked');
            }
            function sharefunc(){
                var a = document.getElementById('agentsharesel').value;
                if (a != '-Select your Agent-'){
                    var b = new XMLHttpRequest();
                    b.open('GET','/share-list/'+a+'/'+'{{obj.id}}');
                    b.send();
                    document.getElementById('agentsharebody').innerHTML = 'Your list has been shared with your agent!'
                }
            }
        
// ================================================================================

        function e(a){
            var b = document.getElementById(a).removeAttribute('readonly');
            // var c = document.getElementById('savesubmit'+a).style = '';
            // var input_id = $(this).attr("id");
                // var list_id = input_id.split("_")[1];
                $("#row" + a + "").css("border", "1px solid #dc3545");
                $("#circle_" + a + "").css("color", "red");
                $("#circle_" + a + "").addClass("text-danger");
                $("#share_" + a + "").css("color", "red");
                $("#share_" + a + "").addClass("text-danger");
                $("#edit_" + a + "").css("color", "red");
                $("#edit_" + a + "" ).removeClass("fa-edit");
                $("#edit_" + a + "").addClass("fa-check text-danger");
                
                $("#" + a+ "").css("background-color", "white");
                $("#" + a + "").hover( function()
                {
                    $("#" + a+ "").css("background-color", "white");
                });
                
                // console.log(a);
        }
        // $(document).on("click", ".fa-check", function()
        // {
        //     // console.log($(this));
        //     form.submit();
        // });

        $('#add').click(function(){
            window.location.href = '{% url "create-list" %}';
        });
        function relocate(a){
            if (document.getElementById(a).hasAttribute('readonly') == true){
                window.location.href = '/show-list/'+a;
            }
        }
        function deletelist(a){
            window.location.href = '/delete-list/'+a;
        }
        $(document).ready(function () {
            var i = 1;

            // Mouseover event for remove...
            $(document).on('mouseover', '.fa-times-circle', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "red");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "white");
            });

            // Mouseout event for remove...
            $(document).on('mouseout', '.fa-times-circle', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "rgb(245, 243, 243)");
            });

            // Mouse over for share ...
            $(document).on('mouseover', '.fa-share-square', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "red");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "white");
            });

            // Mouseout event for share...
            $(document).on('mouseout', '.fa-share-square', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "rgb(245, 243, 243)");
            });

            // Mouse over for edit ...
            $(document).on('mouseover', '.fa-edit', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "red");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "white");
            });

            // Mouseout event for edit...
            $(document).on('mouseout', '.fa-edit', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
                $("#" + button_id.split("_")[1] + "").css("background-color" , "rgb(245, 243, 243)");
            });

            $(document).on('mouseover', '.fa-save', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "red");
            });

            // Mouseout event for edit...
            $(document).on('mouseout', '.fa-save', function () {
                var button_id = $(this).attr("id");
                $("#" + button_id + "").css("color", "black");
            });

            // Click on Remove Button
            $(document).on('click', '.btn-dark', function () {
                var list_id = $(this).attr("id").split("_")[1];
                // $(this).css("background-color" , "red");
                // $(this).css("color" , "white");
                // console.log(button_id);
                // $('#row' + button_id + '').remove();
                if ($("#exampleModalCenter_" + list_id + "").length) {
                    // var A = 
                    // var res = '<p class="card-text text-center">Are you sure you want to delete</p><a class="alert-link text-center mx-auto" href="#">' + $("#lst" + list_id + "").html() + '</a> From your Interest List?'
                    $("#modelBody_" + list_id + "").html('<p class="card-text text-center">Are you sure you want to delete</p><a class="alert-link text-center mx-auto" href="#">' + $("#"+list_id).value + '</a> From your Interest List?' + '<p class="card-text">This action will delete the selected Interest List and all properties within it. If the Interest List was previously shared with your Agent, they will continue to have access to it from their dashboard after you delete it.</p>');
                    $("#modelFooterButton_"+ list_id + "").html("Delete");
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").val());
                    // console.log($("#row" + list_id + "").html());
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").html());
                    $('#exampleModalCenter_' + list_id + '').modal('show');
                    
                }
                else {
                    
                    $("#dynamic_field").prepend('<div class="modal fade" id="exampleModalCenter_' + list_id + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="modelClose_' + list_id + '"><span aria-hidden="true">&times;</span></button></div><div class="modal-body" id="modelBody_' + list_id + '"></div><div class="modal-footer"><button type="button" class="btn btn-danger mx-auto" onclick="deletelist('+list_id+')" id="modelFooterButton_'+ list_id+'"></button></div></div></div></div>');
                    // var res = 
                    $("#modelBody_" + list_id + "").html('<p class="card-text text-center">Are you sure you want to delete</p><a class="alert-link text-center mx-auto" href="/show-list/'+list_id+'">' + document.getElementById(list_id).value  + '</a> From your Interest List?' + '<p class="card-text">This action will delete the selected Interest List and all properties within it. If the Interest List was previously shared with your Agent, they will continue to have access to it from their dashboard after you delete it.</p>');
                    $("#modelFooterButton_"+ list_id + "").html("Delete");
                    // console.log($("#row" + list_id + "").html());
                    // $("#modelBody_" + list_id + "").html($("#row" + list_id + "").html());
                    $('#exampleModalCenter_' + list_id + '').modal('show');
                }

            });

            // on click event for input:

            $(document).on('focus', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid red");
                $("#circle_" + list_id + "").css("color", "red");
                $("#share_" + list_id + "").css("color", "red");
                $("#edit_" + list_id + "").css("color", "red");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('click', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid red");
                $("#circle_" + list_id + "").css("color", "red");
                $("#share_" + list_id + "").css("color", "red");
                $("#edit_" + list_id + "").css("color", "red");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('focusin', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid red");
                $("#circle_" + list_id + "").css("color", "red");
                $("#share_" + list_id + "").css("color", "red");
                $("#edit_" + list_id + "").css("color", "red");
                $("#" + list_id + "").css("background-color", "white");
            });

            $(document).on('focusout', ".form-control", function () {
                var input_id = $(this).attr("id");
                var list_id = input_id.split("_")[1];
                $("#row" + list_id + "").css("border", "1px solid rgba(0,0,0,.125)");
                $("#circle_" + list_id + "").css("color", "black");
                $("#share_" + list_id + "").css("color", "black");
                $("#edit_" + list_id + "").css("color", "black");
            });

            // Click on Share Button
                // $("#share_" + list_id + "").css("color", "black");
                // $('#share_'+list_id+"").css("color", "red");
                // console.log(list_id);
                // $("#share_" + list_id + "").css("color", "red");
                
            // // Mouseout event for share...
            // $(document).on('mouseout', '.fa-share-square', function () {
            //     var button_id = $(this).attr("id");
            //     $("#" + button_id + "").css("color", "red");
            // });
            });

// ================================================================================