from os import system, path
from sys import argv, stderr, exit

if len(argv) != 3:
	stderr.write('Usage: {} <text_filename> <xml_filename>\n'.format(argv[0]))
	exit(1)

input_filename = argv[1]
output_filename = argv[2]

# constants
ROOT_DIR = '/Users/Anna/Desktop/VKR_Goncharova'
DATA_DIR = path.join(ROOT_DIR, 'data')
WARP_DIR = path.join(ROOT_DIR, 'warp')

# nkrya xml parser
xml_parser_script = path.join(WARP_DIR, 'parse_xml_to_json.py')
nkrya_result = path.join(DATA_DIR, 'nkrya.json')
system('python {} {} {}'.format(xml_parser_script, argv[2], nkrya_result))

# run main program
runner_script = path.join(WARP_DIR, 'runner.py')
print('Stay calm, my program is running!')
my_result = path.join(DATA_DIR, 'my_result.json')
system('python {} {} {}'.format(runner_script, argv[1], my_result))

# compare files
compare_script = path.join(WARP_DIR, 'compare_files.py')
system('python {} {} {}'.format(compare_script, nkrya_result, my_result))
