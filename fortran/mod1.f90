module mod1
  use mod2
  implicit none
contains


subroutine test(arg)
  implicit none
  integer, intent(in) :: arg
end subroutine test


end module mod1


