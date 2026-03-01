-- eq-table.lua
-- 將 $$...\tag{X-Y}$$ 轉換為 1×3 表格（空白 | 公式置中 | 編號靠右）
-- 用法: pandoc input.md -o output.docx --lua-filter=eq-table.lua

function Para(el)
  -- 檢查段落是否只包含一個 DisplayMath
  if #el.content == 1
    and el.content[1].t == "Math"
    and el.content[1].mathtype == "DisplayMath" then

    local text = el.content[1].text
    local tag = text:match("\\tag{(.-)}")
    if not tag then return nil end

    -- 移除 \tag{...}
    local math_clean = text:gsub("%s*\\tag{.-}%s*", "")

    -- 用 markdown pipe table 產生表格（header 留空，內容放 body）
    local md = string.format(
      "|   |   |   |\n|---|:---:|---:|\n|   | $%s$ | (%s) |",
      math_clean, tag
    )

    local doc = pandoc.read(md, "markdown")
    if #doc.blocks > 0 then
      return doc.blocks[1]
    end
  end
end
