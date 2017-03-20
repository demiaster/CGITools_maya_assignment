alias s="rclone sync --size-only -v --retries 50"
local today=$(date +%Y%m%d)
local yesterday=$(date -d yesterday +%Y%m%d)
s hubic:default/Arctic-$yesterday hubic:default/Arctic-$today
s gdrive:Arctic hubic:default/Arctic-$today
