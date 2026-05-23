async function loadData() {

  try {

    const response = await fetch("https://ims-cclz.onrender.com");

    const data = await response.json();

    document.getElementById("level").innerText =
      data.level + " %";

    document.getElementById("temp").innerText =
      data.temperature + " °C";

    document.getElementById("status").innerText =
      data.status;

  } catch (error) {

    console.log(error);

  }

}

loadData();

setInterval(loadData, 5000);
