//GET
function getValueInput() {
  const inputUsername = document.getElementById('inputUsername').value
  document.getElementById("searchbtn").onclick = function () {

    const url = new URL('http://127.0.0.1:5000/api/members')
    const params = {username: inputUsername} 
    url.search = new URLSearchParams(params).toString();

    fetch(url)
      .then((response) => {
        return response.json();
      })
      .then((result) => {
        if (result.data != null) {
          document.getElementById('showSearchData').innerHTML = result.data.name + '(' + result.data.username + ')';
        }
        else {
          document.getElementById('showSearchData').innerHTML = '無此會員';
        }
      })
      .catch((error) => {
        console.log('error', error)
      })
  };
}

//POST
function getUpdateValueInput() {
  const updateName = document.getElementById('updateName').value
  document.getElementById("updatehbtn").onclick = function () {
    console.log(updateName)

    fetch("http://127.0.0.1:5000/api/member", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "name": updateName
      })
    })
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      console.log('result', result)
      document.getElementById('showUpdateData').innerHTML = '更新成功';
    })
    .catch((error) => {
      console.log('error', error)
      document.getElementById('showUpdateData').innerHTML = '更新失敗';
    })
  };
}