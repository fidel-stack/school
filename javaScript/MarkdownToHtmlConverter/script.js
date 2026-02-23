function convertMarkdown (){
  const input = document.getElementById("markdown-input").value;
  let output = input;

  //code
  output = output.replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>");

  //headings
  output = output.replace(/^\s*###\s+(.*)$/gm, "<h3>$1</h3>");
  output = output.replace(/^\s*##\s+(.*)$/gm, "<h2>$1</h2>");
  output = output.replace(/^\s*#\s+(.*)$/gm, "<h1>$1</h1>");

  //unordered list
  output = output.replace(/(?:^\s*-\s+(.*)$\n?)+/gm,match => {
    const items = match
    .trim()
    .split("\n")
    .map(i => `<li>${i.replace(/^\s*-\s+/, "")}</li>`)
    .join("");
    return `<ul>${items}</ul>`;
  });
  //ordered list
  output = output.replace(/(?:^\s*\d+\.\s+(.*)$\n?)+/gm, match => {
    const items = match
    .trim()
    .split("\n")
    .map(i => `<li>${i.replace(/^\s*\d+\.\s+/, "")}</li>`)
    .join("");
    return `<ol>${items}</ol>`;
  });

  //blockquote
  output = output.replace(/^\s*>\s+(.*)$/gm, "<blockquote>$1</blockquote>");

    //horizontal rule
  output = output.replace(/^\s*---\s*$/gm, "<hr>");

  //images
  output = output.replace(/!\[(.*?)\]\((.*?)\)/g, '<img alt="$1" src="$2">');

  //links
  output = output.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>');

  //bold
  output = output.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  output = output.replace(/__(.*?)__/g, "<strong>$1</strong>");

  //italic
  output = output.replace(/\*(.*?)\*/g, "<em>$1</em>");
  output = output.replace(/_(.*?)_/g, "<em>$1</em>");

  //strike through
  output = output.replace(/~~(.*?)~~/g, "<s>$1</s>");

  return output;
}

document.getElementById("markdown-input").addEventListener("input", () => {
  const html = convertMarkdown();

  document.getElementById("html-output").textContent = html;
  document.getElementById("preview").innerHTML = html;
});