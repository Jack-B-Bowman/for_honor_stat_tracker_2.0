$date = Get-Date -Format "MM-dd-yyyy-HH-mm"
Set-Location 'C:\Users\Jack Bowman\Documents\Programs\PytScripts\UbiScraper\for_honor_stat_tracker_2.0'
C:\ProgramData\Anaconda3\python.exe '.\get_user_ids.py'
C:\ProgramData\Anaconda3\python.exe '.\merge_player_id_files.py'
Set-Location 'C:\Users\Jack Bowman\Documents\Programs\PytScripts\UbiScraper\for_honor_stat_tracker_2.0\player_id_files'
C:\'Program Files'\7-Zip\7z.exe a -sdel "D:\Archive\for_honor_stat_tracker_2.0\userFiles$date" .