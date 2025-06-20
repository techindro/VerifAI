// Example fetch call (you can run from browser console or button)
fetch("/api/fake-news", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ text: "Some fake news headline..." })
})
.then(res => res.json())
.then(data => console.log(data));
