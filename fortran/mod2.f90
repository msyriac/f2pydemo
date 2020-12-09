module mod2
  implicit none

  !* I think this makes it impossible to f2py this module
  type test_struct
    integer :: n
  end type test_struct

contains

function test2(arg) result(d)
  implicit none
  integer, intent(in) :: arg
  double precision :: d(2)

end function test2


end module mod2


