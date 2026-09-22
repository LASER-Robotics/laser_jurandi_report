document.addEventListener("DOMContentLoaded", () => {
  const article = document.querySelector(".wy-nav-content");
  if (article) article.id = "documentacao";
  document.querySelectorAll("table.docutils").forEach((table) => {
    if (!table.parentElement?.classList.contains("table-scroll")) {
      const wrapper = document.createElement("div");
      wrapper.className = "table-scroll";
      table.parentNode?.insertBefore(wrapper, table);
      wrapper.appendChild(table);
    }
  });
});
