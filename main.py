import os
import argparse


def main(args):
   i = 0
   input_path = args.input
   output_path = args.output
   if output_path is not None and not os.path.exists(output_path):
      os.makedirs(output_path)

   if output_path is None:
      output_path = input_path

   print("Input folder path: ", input_path)
   print("Output folder path: ", output_path)

   if args.extension is None:
      file_extension = ""
      print("Rename all file")
   else:
      file_extension = "." + args.extension.split(".")[-1]
      print(f"Rename file with {file_extension}\n")

   i = 0
   for filename in os.listdir(input_path):
      if filename.endswith(file_extension):
         src_filename = filename
         src_extension = src_filename.split(".")[-1]

         dst_filename = args.name + "_" if args.name is not None else ""
         dst_filename += "{:04d}.{}".format(i, src_extension)

         src = os.path.join(input_path, src_filename)
         dst = os.path.join(output_path, dst_filename)
         print(f"Rename file '{src_filename}' to '{dst_filename}'")

         os.rename(src, dst)
         i += 1


if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Batch rename file\n")
   parser.add_argument('-i', '--input', type=str, required=True, help='input folder path')
   parser.add_argument('-o', '--output', type=str, help='Output folder path')
   parser.add_argument('-n', '--name', type=str, help='file name format')
   parser.add_argument('-e', '--extension', type=str, help='rename the specified extension file')
   args = parser.parse_args()

   main(args)