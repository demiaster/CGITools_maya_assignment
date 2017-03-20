require 'fileutils'

ext = ARGV[2] || 'exr'
fname = ARGV[1] || "SH_01.mantra_ipr"
offset = ARGV[0].to_i || 2000

FileUtils.mkdir_p('out')
Dir.chdir('out') do
	Dir["../#{fname}.*.#{ext}"].each do |f|
		oldnum = f.gsub(fname,'').gsub(fname,'')[/\d+/].to_i
		newnum = oldnum + offset
		FileUtils.cp(f, "./#{fname}.#{newnum}.#{ext}")
	end
end
