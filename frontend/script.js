async function loadData() {
  const res = await fetch("/data");
  const data = await res.json();
  const list = document.getElementById("list");
  list.innerHTML = "";
  data.data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
}
