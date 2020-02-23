// ====================================================================

setInterval(
function func1(){
    document.getElementById('listnameinmodal').innerHTML =  document.getElementById('listHeading_'+document.getElementById('move2').value).innerHTML;
    document.getElementById('listnameinmodal1').innerHTML =  document.getElementById('dropDownList_0001_'+document.getElementById('move1').value).innerHTML;
},500
)
setInterval(
function func2(){
    document.getElementById('listnameinmodaldel').innerHTML =  document.getElementById('listHeading_'+document.getElementById('del1').value).innerHTML;
},500
)
function newfunc1(){
setTimeout(
    function(){
        var a = document.getElementById('move1').value;
        var b = document.getElementById('move2').value;
        window.location.href = '/addfromlist/'+a+'/'+b+'/'+'{{obj.id}}';
    },4000)
}
function delfunc(){
var a = document.getElementById('del1').value;
window.location.href = '/remove-from-list/{{obj.id}}/'+a;
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
function funcrate(a,b){
if (b == '0'){
    document.getElementById(a+'happy').style.color = 'red';
    document.getElementById(a+'happy1').style.color = 'white';
    document.getElementById(a+'happy2').style.color = 'white';
}
if (b == '1'){
    document.getElementById(a+'happy1').style.color = 'red';
    document.getElementById(a+'happy').style.color = 'white';
    document.getElementById(a+'happy2').style.color = 'white';
}
if (b == '2'){
    document.getElementById(a+'happy2').style.color = 'red';
    document.getElementById(a+'happy1').style.color = 'white';
    document.getElementById(a+'happy').style.color = 'white';
}
var c = new XMLHttpRequest();
c.open('GET','/rate/{{obj.id}}/'+a+'/'+b);
c.send();
}

// =====================================================================

// ===================================================================

function removal(a,b){
window.location.href = '/remove-from-list/'+a+'/'+b;
}

$(document).ready(function () {

// mouseover event for a list element
$(document).on("mouseover", ".list-group-item-action", function () {
$("#listHeading_" + $(this).attr("id").split("_")[1] + "").css("color", "red");
$("#buttonImageA_" + $(this).attr("id").split("_")[1] + "").css("display", "block");
$("#buttonImageB_" + $(this).attr("id").split("_")[1] + "").css("display", "block");
});

//   mouseout event for a list element
$(document).on("mouseout", ".list-group-item-action", function () {
$("#listHeading_" + $(this).attr("id").split("_")[1] + "").css("color", "black");
$("#buttonImageA_" + $(this).attr("id").split("_")[1] + "").css("display", "none");
$("#buttonImageB_" + $(this).attr("id").split("_")[1] + "").css("display", "none");
});

$(document).on("click", ".btn-white", function () {
var i = $(this).attr("id").split("_");
if (i[0] == "lsteditButtonEdit") {
if ($("#lsteditButtonSubmit_" + i[1] + "").css("display") == "none") {
$("#lsteditButtonSubmit_" + i[1] + "").css("display", "block");
$("#lstNotesText_" + i[1] + "").removeAttr("readonly");
}
else {
$("#lsteditButtonSubmit_" + i[1] + "").css("display", "none");
$("#lstNotesText_" + i[1] + "").attr("readonly", "true");
}

}
});

$(document).on("click", ".btn-white", function () {
var i = $(this).attr("id").split("_");
if (i[0] == "propertyNotesEdit") {
$("#propertyNotes_" + i[1] + "").removeAttr("readonly");
$("#propertyNotes_" + i[1] + "").addClass("border-1");
$("#propertyNotes_" + i[1] + "").removeClass("border-0");
$("#propertyNotesEditSubmit_" + i[1] + "").css("display", "block");
$("#propertyNotesEdit_" + i[1] + "").css("display", "none");
}
else if (i[0] == "propertyNotesEditSubmit") {
$("#propertyNotesEditSubmit_" + i[1] + "").css("display", "none");
$("#propertyNotesEdit_" + i[1] + "").css("display", "block");
$("#propertyNotes_" + i[1] + "").attr("readonly", "true");
$("#propertyNotesForm_" + i[1] + "").submit();
}
});

// CLick event on dropdown list...
$(document).on("click", ".list-group-item", function(){
var i = $(this).attr("id").split("_");
// console.log(i);
// console.log(lst_id);
if(i[0] == "dropDownList"){
// console.log($("#lst_" + i[1]));
if($('#exampleModalCenter_' + i[1] + '_' + i[2]+ '').length == 0)
{
// $("#propertyListDropDownForm_" + i[1] + "").submit();
$("#lst_" + i[1] +  "").before('<div class="modal fade" id="exampleModalCenter_'+i[1]+'_'+ i[2]+'" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"> <div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content"> <div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="CloseModel_' + i[1] + '_' + i[2] + '"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center mt-0" style="color: red; font-size: 20px;"><a href="#" class="text-decoration" style="color: red;" id="exampleModalCenterLinkA_'+ i[1] + '_' + i[2] + '"></a><br><span style="color: black;">has been moved to</span><br><a href="#" style="color: red;" id="exampleModalCenterLinkB_'+ i[1] + '_' + i[2] + '"></a></div></div></div></div>')
$("#exampleModalCenterLinkA_" + i[1] + "_" + i[2] + "").html($("#listHeading_" + i[1] +   "").html());
$('#exampleModalCenter_' + i[1] + '_' + i[2]+ '').modal('show');
$("#exampleModalCenterLinkB_" + i[1] + "_" + i[2] + "").html($("#" + $(this).attr("id") + "").html());

}
else{
// $("#exampleModalCenterLinkA_" + i[1] + "").html($("#" + $(this).attr("id") + "-").html());
$("#exampleModalCenterLinkB_" + i[1] + "_" + i[2] + "").html($("#" + $(this).attr("id") + "").html());
$("#exampleModalCenterLinkA_" + i[1] + "_" + i[2] + "").html($("#listHeading_" + i[1] +   "").html());
$('#exampleModalCenter_' + i[1] + '_' + i[2]+ '').modal('show');
// $("#propertyListDropDownForm_" + i[1] + "").submit();
}

}
});

$(document).on("click", ".close", function()
{
var i = $(this).attr("id").split("_");
// console.log($(this).attr("id"));
if(i[0] == "CloseModel"){
$("#propertyListDropDownForm_" + i[1] + "").submit();   
}
});

// Model Remove Button ...

$(document).on("click", ".btn-white", function()
{
var i = $(this).attr("id").split("_");
console.log(i);
if(i[0] == "exampleModalCenterRemoveButton")
{
if($("#exampleModalCenterRemove_"+ i[1]+ "").length == 0){
$("#lst_" + i[1] +  "").before('<div class="modal fade text-center" id="exampleModalCenterRemove_' + i[1] + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"> <div class="modal-dialog modal-dialog-centered" role="document"> <div class="modal-content text-center"><div class="modal-header border-0 text-center"><h5 class="modal-title text-center pl-5" id="exampleModalCenterTitle">Are you sure you want to remove</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body border-0" id="exampleModalCenterRemoveBody_'+i[1]+'"></div><div class="modal-footer border-0 mx-auto"><button type="button" onclick="removal({{obj.id}},'+i[2]+')" class="btn btn-primary bg-danger p-2 ">Remove</button></div></div></div></div>');
// var s = '<a href="#">' + $("#listHeading_" + i[1] + "").html() + '</a>';
$("#exampleModalCenterRemoveBody_" + i[1]+ "").html('<a href="/property-detail/'+i[2]+'">' + $("#listHeading_" + i[2] + "").html() + '</a><br> from &nbsp; <a href="#">' + $("#property_title").html()+'</a>');
$("#exampleModalCenterRemove_" + i[1] + "").modal("show");
}
else{
$("#exampleModalCenterRemoveBody_" + i[1]+ "").html('<a href="#">' + $("#listHeading_" + i[1] + "").html() + '</a><br>from &nbsp; <a href="#">' + $("#property_title").html()+'</a>');
$("#exampleModalCenterRemove_" + i[1] + "").modal("show");
}
}
});

$(document).on("click", ".float-right", function(){
var i = $(this).attr("id");
// console.log(i);
if(i == "proper_actions")
{
if($("#proper_actions_list").css("display") == "none"){
$("#proper_actions_list").css("display", "block");
}   
else{
$("#proper_actions_list").css("display", "none");
}
}
});

// CLick event for share interest list ....
$(document).on("click", '.list-group-item', function()
{
var i = $(this).attr("id").split("_");
// console.log(i);
if(i[0] == "ShareWithAgent"){
if($("#exampleModalCenterShareWithAgent_" + i[1] + "").length==0){
$("#lst_" + i[1] + "").before('<div class="modal fade" id="exampleModalCenterShareWithAgent_' + i[1] + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered text-center" role="document"><div class="modal-content text-center"><div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="0001"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center"><a href="#">' + $("#property_title").html() + '</a>  is ready to be shared with your UpClinch Agent</div> <div class="modal-footer text-center border-0" style="padding-right:45%;"><button type="button" class="btn btn-danger p-1 text-center" data-dismiss="modal" >Share</button></div></div></div></div>');
$("#exampleModalCenterShareWithAgent_" + i[1] + "").modal("show");
}
else{
$("#exampleModalCenterShareWithAgent_" + i[1] + "").modal("show");
}

}
});

// Click event for complete review
$(document).on("click", '.list-group-item', function()
{
var i = $(this).attr("id").split("_");
// console.log(i);
if(i[0] == "CompleteReview"){
if($("#exampleModalCenterCompleteReview_" + i[1] + "").length==0){
$("#lst_" + i[1] + "").before('<div class="modal fade" id="exampleModalCenterCompleteReview_' + i[1] + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered text-center" role="document"><div class="modal-content text-center"><div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="0001"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center">You have successfully complete your review of <br><a href="#">' + $("#property_title").html() + '</a><br>Your UpClinch Agent has been notified. Thanks!</div></div></div></div>');
$("#exampleModalCenterCompleteReview_" + i[1] + "").modal("show");
}
else{
$("#exampleModalCenterCompleteReview_" + i[1] + "").modal("show");
}

}
});

// Click event for Delete
$(document).on("click", '.list-group-item', function()
{
var i = $(this).attr("id").split("_");
console.log(i);
if(i[0] == "DeleteInterstList"){
if($("#exampleModalCenterDeleteInterstList_" + i[1] + "").length==0){
$("#lst_" + i[1] + "").before('<div class="modal fade" id="exampleModalCenterDeleteInterstList_' + i[1] + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered text-center" role="document"><div class="modal-content text-center"><div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="0001"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center">Are you sure you want to delete <br><a href="#">' + $("#property_title").html() + '</a><br>This section will delete the selected Interest List and all properties within it. If the Interest List was previously shared with your Agent, they wil continue to have access to it from their dashboard after you delete it.</div><div class="modal-footer text-center border-0" style="padding-right:45%;"><button type="button" class="btn btn-danger p-2 m-1 text-center" data-dismiss="modal" onclick="deletelist()">Delete</button></div></div></div></div>');
$("#exampleModalCenterDeleteInterstList_" + i[1] + "").modal("show");
}
else{
$("#exampleModalCenterDeleteInterstList_" + i[1] + "").modal("show");
}      
}
});

// Incase of incomplete review...
$(document).on("click", ".list-group-item" , function()
{
var i = $(this).attr("id").split("_");
if(i[0] == "InCompleteReview"){
if($("#exampleModalCenterInCompleteReview_" + i[1] + "").length == 0)
{
$("#lst_" + i[1] + "").before('<div class="modal fade" id="exampleModalCenterInCompleteReview_' + i[1] + '" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered text-center" role="document"><div class="modal-content text-center"><div class="modal-header border-0"><button type="button" class="close" data-dismiss="modal" aria-label="Close" id="0001"><span aria-hidden="true">&times;</span></button></div><div class="modal-body text-center">Please review each property in <a href="#">' + $("#property_title").html() + '</a><br>invidually in order to Complete Review of this Interest List.Thanks!</div><div class="modal-footer text-center border-0" style="padding-right:45%;"><button type="button" class="btn btn-danger p-2 m-1 text-center" data-dismiss="modal" >Delete</button></div></div></div></div>');
$("#exampleModalCenterInCompleteReview_" + i[1] + "").modal("show");
}
else{
$("#exampleModalCenterInCompleteReview_" + i[1] + "").modal("show");
}
}
});

// Waste Material .......................

// click event or drop down
// $(document).on("click", ".btn-white" , function()
// {
//     // console.log("1");
//     var i = $(this).attr("id").split("_");
//     console.log(this);
//     if(i[0] == "dropdownMenuButton")
//     {
//         if($("#propertyListDropDownForm_"+ i[1] + "").length == 0)
//         {
//             $("#dropdownMenuButton_" + i[1] + "").append('<form id="propertyListDropDownForm_'+i[1]+'" method="POST"><div class="dropdown-menu overflow-auto p-0" aria-labelledby="dropdownMenuButton_'+i[1]+'" style="height:100px;" id="dropdownMenu_'+i[1] + '"><li class="list-group-item list-group-item-action" name="drop"  id="dropDownList_'+i[1]+'_1">Cras justo odio</li><li class="list-group-item list-group-item-action" name="drop"  id="dropDownList_'+i[1]+'_2">Dapibus ac facilisis in</li><li class="list-group-item list-group-item-action" name="drop"  id="dropDownList_'+i[1]+'_3">Morbi leo risus</li><li class="list-group-item list-group-item-action" name="drop"  id="dropDownList_'+i[1]+'_4">Porta ac consectetur ac</li><li class="list-group-item list-group-item-action" name="drop" id="dropDownList_'+i[1]+'_5">Vestibulum at eros</li></div></form>')
//             $("#dropdownMenu_" + i[1]+ "").dropdown("show");
//         }
//         else{
//             $("#dropdownMenu_" + i[1]+ "").dropdown("show");
//         }
//         // console.log("1");
//         // dropdownMenuButton

//     }

// });

// submit button for dropdown
// $(document).on("click", ".list-group-item", function()
// {
//     // propertyListDropDown_0001
//     var i = $(this).attr("id").split("_");
//     // console.log(i);
//     if(i[0] == "dropDownList")
//     {
//         // console.log("1");
//         // console.log($("#propertyListDropDownForm_" + i[1] + ""));
//         $("#propertyListDropDownForm_" + i[1] + "").submit();
//     }
// });

// $(document).on("click", ".btn-white", function(){
//     var i = $(this).attr("id").split("_");
//     if(i[0] == "propertyNotesEdit"){
//         $("#propertyNotesEditSubmit_" + i[1] + "").css("display", "block");
//         $("#propertyNotesEdit_" + i[1] + "").css("display", "none");
//     }
//     else if(i[0] == "propertyNotesEditSubmit"){
//         $("#propertyNotesEditSubmit_" + i[1] + "").css("display", "none");
//         $("#propertyNotesEdit_" + i[1] + "").css("display", "block");
//     }
// });
// $(document).on("click", ".btn-white", function () {
//     var i = $(this).attr("id").split("_")[1];
//     $("#lstNotesText_" + i + "").removeAttr("readonly");
//     console.log(i);

//         $("#lsteditButton_" + i + "").append('<button id="submitListNote_"' + i + '" class="btn btn-white float-right" style="display:block;">Submit</button>')

// });

// $(document).on("click", ".btn-white", function(){
//     if($(this).attr("id").split("_")[0] == "submitListNote"){
//         $("submitListNote_" + $(this).attr("id").split("_")[1] + "").click();
//     }

//     });

// });
// $('#submit').click(function () {
//     $.ajax({
//         url: "name.php",
//         method: "POST",
//         data: $('#add_name').serialize(),
//         success: function (data) {
//             alert(data);
//             $('#add_name')[0].reset();
//         }
//     });

// });

});

// ====================================================================