# Disclang

No libraries required all you need is the latest version of python

Bad Docs (with example):
`:k6
Okay heres the basic syntax
--<mode> sets mode; import, init, main
:: note
:k[<num>] multi line note
<command>[<arg>] command
>><name> export a module

--import
>>chat
>>reply
>>activity
>>out
--init
activity-[1][Minecraft]
out-[Started!]
--main
chat-[Hello][World!]
chat-[I like cats!][yo me too]
chat-[uwu][shut]

:k150
******* BUILT IN ********
*chat and reply:
chat[arg][arg2]
reply[arg][arg2]
sends arg2 when arg is said, example:
chat[Hello][World!]
responds to Hello with World!
*activity:
activity[arg1][arg2]
arg1 is 1-4 arg2 is the string to be displayed after
1: Playing arg2
2: Streaming arg2
3: Listening to arg2
4: Watching arg2
out[arg]
print('arg')
Eg, out[Hello World!]
console: Hello World!

by the way, you can safely do :k150 because it only checks in the loop (for every line in the script) so it wont go on for another 150 lines`
