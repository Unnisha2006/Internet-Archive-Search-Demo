async function search() {
    let q = document.getElementById("q").value;

    let res = await fetch(`http://127.0.0.1:8000/search?q=${q}`);
    let data = await res.json();

    let html = "";

    data.results.forEach(book => {
        html += `
          <div class="card">
            <h3>${book.title}</h3>
            <p>${book.author} (${book.year})</p>
          </div>
        `;
    });

    document.getElementById("results").innerHTML = html;
}