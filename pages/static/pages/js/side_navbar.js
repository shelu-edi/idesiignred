// $(".sidebar-dropdown > a").click(function() {
//   $(".sidebar-submenu").slideUp(250);
//   if (
//     $(this)
//       .parent()
//       .hasClass("active")
//   ) {
//     $(".sidebar-dropdown").removeClass("active");
//     $(this)
//       .parent()
//       .removeClass("active");
//   } else {
//     $(".sidebar-dropdown").removeClass("active");
//     $(this)
//       .next(".sidebar-submenu")
//       .slideDown(250);
//     $(this)
//       .parent()
//       .addClass("active");
//   }
// });

// $("#toggle-sidebar").click(function() {
//   $(".page-wrapper").toggleClass("toggled");
// });

$(document).ready(function () {

    $("#sidebar").mCustomScrollbar({
         theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        // open or close navbar
        $('#sidebar').toggleClass('active');
        // close dropdowns
        $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });

});