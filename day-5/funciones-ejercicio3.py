def validate_zero_duplicate(*args):
   if( 0 in args ):
      # Get the index where 0 is
      zero_index = args.index(0)
      if ( args[zero_index + 1] == 0 ):
         return True
      else:
         return False
   else:
      return False

print(validate_zero_duplicate(1, 4, 0, 0))