$("document").ready(function () {
  $.ajax({
    type: "GET",
    url: "http://0.0.0.0:5001/api/v1/cities",
    success: function (data) {
      const info = data;
      let names = [];
      for (i in info) {
        if (info[i]["__class__"] == "City") {
          names.push(info[i]["name"]);
        }
      }
      names.sort(function (a, b) {
        return a.localeCompare(b);
      });
      for (let j = 0; j < names.length; j++) {
        let name = names[j];
        /*for (i in info) {
          let ids = "";
          if (info[i]["name"] == name) {
            ids = info[i]["id"];
            break;
          } else {
            continue;
          }
        }*/
        $(".city-details select").append(
          '<option value="' + name + '">' + name + "</option>"
        );
      }
    },
  });
});
