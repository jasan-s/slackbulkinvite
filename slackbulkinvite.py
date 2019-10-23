var foundAny=false;
function selectAllByLetter(remainingLetters) {
  console.log(remainingLetters)
  var letter = remainingLetters.pop();
  $("#channel_invite_filter").val(letter).trigger("input");
  setTimeout(function() {
    $(".channel_invite_member:not(hidden)").each(function(i, obj) {
        foundAny=true;
        this.click();
    });
    if (remainingLetters.length) {
      selectAllByLetter(remainingLetters);
    } else {
      setTimeout(function() {
        console.log("Inviting them all!")
        $('.invite_go').click()
      },400)     
    }
  },300);
}

function inviteAllUsers() {      
  foundAny=false;     
  setTimeout(function () {    
      setTimeout(function() {
        $('#channel_actions_toggle').click();
      },100)
      setTimeout(function() {
        $('#channel_invite_item').click();
      },200)
      //Enter each letter to trigger searches
      var remainingLetters = ["a","b","c","d","e","f","g","h","i","j","v","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
      selectAllByLetter(remainingLetters);
      if (foundAny) {
        inviteAllUsers();
      }
   }, 4000);
}

inviteAllUsers();  
