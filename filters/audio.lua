--[[
  audio.lua

  Attaches a recording to any code block that declares one:

      ```{.ruby audio="L07-1.mp3"}
      play :c4
      ```

  In HTML the block is followed by a player. In PDF and EPUB a player is no
  use, so the block is followed by a QR code linking to the recording on the
  website, falling back to a printed URL when the QR image has not been
  generated yet. Run scripts/make-audio.sh to produce both the mp3 and the QR.

  The base URL comes from `audio-base-url` in _quarto.yml.
]]

local audio_base = ""
local audio_dir = "assets/audio/"

local function get_meta(meta)
  if meta["audio-base-url"] then
    audio_base = pandoc.utils.stringify(meta["audio-base-url"])
  end
  return nil
end

-- Cheapest reliable existence check available to a Lua filter.
local function file_exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

-- How many directories deep the current lesson sits, as a "../../" prefix.
--
-- A site-root path like /assets/audio/x.mp3 breaks on GitHub Pages project
-- sites, which serve from /<repo>/ rather than from the domain root, and
-- Quarto does not rewrite the src attribute of raw HTML the way it rewrites
-- href. Computing the path relative to the document sidesteps both problems.
local function up_to_root()
  local input = quarto.doc.input_file
  local root = quarto.project.directory
  if not input or not root then return "" end

  local rel = input:sub(#root + 2)          -- drop the root and its slash
  local dir = rel:match("^(.*)/[^/]*$")     -- directory part, nil at top level
  if not dir then return "" end

  local prefix = ""
  for _ in dir:gmatch("[^/]+") do prefix = prefix .. "../" end
  return prefix
end

local function handle(block)
  local name = block.attributes["audio"]
  if not name or name == "" then
    return nil
  end

  -- Drop the attribute so it does not surface as a stray class in the output.
  block.attributes["audio"] = nil

  if quarto.doc.is_format("html:js") then
    local src = up_to_root() .. audio_dir .. name
    local player = string.format(
      '<div class="sonic-audio"><audio controls preload="none" src="%s">' ..
      '<a href="%s">Download the recording</a></audio></div>',
      src, src
    )
    return pandoc.Div(
      { block, pandoc.RawBlock("html", player) },
      pandoc.Attr("", { "sonic-example" })
    )
  end

  local url = audio_base .. name
  local qr = audio_dir .. "qr/" .. name:gsub("%.%w+$", "") .. ".png"

  if file_exists(qr) then
    local img = pandoc.Image({ pandoc.Str("Listen") }, qr, "Listen: " .. url)
    img.attributes["width"] = "2.2cm"
    return { block, pandoc.Para({ img, pandoc.Space(), pandoc.Emph({ pandoc.Str("Listen:") }),
                                 pandoc.Space(), pandoc.Str(url) }) }
  end

  return { block, pandoc.Para({ pandoc.Emph({ pandoc.Str("Listen:") }),
                                pandoc.Space(), pandoc.Str(url) }) }
end

return {
  { Meta = get_meta },
  { CodeBlock = handle },
}
