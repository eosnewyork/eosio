(module
 (type $FUNCSIG$vi (func (param i32)))
 (type $FUNCSIG$vj (func (param i64)))
 (type $FUNCSIG$iii (func (param i32 i32) (result i32)))
 (type $FUNCSIG$vii (func (param i32 i32)))
 (import "env" "eosio_assert" (func $eosio_assert (param i32 i32)))
 (import "env" "printn" (func $printn (param i64)))
 (import "env" "prints" (func $prints (param i32)))
 (import "env" "read_action" (func $read_action (param i32 i32) (result i32)))
 (table 0 anyfunc)
 (memory $0 1)
 (data (i32.const 4) "@a\00\00")
 (data (i32.const 16) "Hello World: \00")
 (data (i32.const 32) " asked \00")
 (data (i32.const 48) "create\00")
 (data (i32.const 64) "action shorter than expected\00")
 (data (i32.const 96) "->\00")
 (data (i32.const 112) "\n\00")
 (export "memory" (memory $0))
 (export "_ZN7hw_poll12apply_createERKNS_6createE" (func $_ZN7hw_poll12apply_createERKNS_6createE))
 (export "apply" (func $apply))
 (export "free" (func $free))
 (func $_ZN7hw_poll12apply_createERKNS_6createE (param $0 i32)
  (local $1 i64)
  (set_local $1
   (i64.load align=1
    (get_local $0)
   )
  )
  (block $label$0
   (block $label$1
    (br_if $label$1
     (i32.and
      (i32.load8_u offset=8
       (get_local $0)
      )
      (i32.const 1)
     )
    )
    (set_local $0
     (i32.add
      (i32.add
       (get_local $0)
       (i32.const 8)
      )
      (i32.const 1)
     )
    )
    (br $label$0)
   )
   (set_local $0
    (i32.load
     (i32.add
      (get_local $0)
      (i32.const 16)
     )
    )
   )
  )
  (call $prints
   (i32.const 16)
  )
  (call $printn
   (get_local $1)
  )
  (call $prints
   (i32.const 32)
  )
  (call $prints
   (get_local $0)
  )
 )
 (func $apply (param $0 i64) (param $1 i64)
  (local $2 i32)
  (local $3 i32)
  (local $4 i32)
  (local $5 i64)
  (local $6 i64)
  (local $7 i64)
  (local $8 i64)
  (local $9 i32)
  (i32.store offset=4
   (i32.const 0)
   (tee_local $9
    (i32.sub
     (i32.load offset=4
      (i32.const 0)
     )
     (i32.const 32)
    )
   )
  )
  (set_local $6
   (i64.const 0)
  )
  (set_local $5
   (i64.const 59)
  )
  (set_local $4
   (i32.const 48)
  )
  (set_local $7
   (i64.const 0)
  )
  (loop $label$0
   (block $label$1
    (block $label$2
     (block $label$3
      (block $label$4
       (block $label$5
        (br_if $label$5
         (i64.gt_u
          (get_local $6)
          (i64.const 5)
         )
        )
        (br_if $label$4
         (i32.gt_u
          (i32.and
           (i32.add
            (tee_local $2
             (i32.load8_s
              (get_local $4)
             )
            )
            (i32.const -97)
           )
           (i32.const 255)
          )
          (i32.const 25)
         )
        )
        (set_local $2
         (i32.add
          (get_local $2)
          (i32.const 165)
         )
        )
        (br $label$3)
       )
       (set_local $8
        (i64.const 0)
       )
       (br_if $label$2
        (i64.le_u
         (get_local $6)
         (i64.const 11)
        )
       )
       (br $label$1)
      )
      (set_local $2
       (select
        (i32.add
         (get_local $2)
         (i32.const 208)
        )
        (i32.const 0)
        (i32.lt_u
         (i32.and
          (i32.add
           (get_local $2)
           (i32.const -49)
          )
          (i32.const 255)
         )
         (i32.const 5)
        )
       )
      )
     )
     (set_local $8
      (i64.shr_s
       (i64.shl
        (i64.extend_u/i32
         (get_local $2)
        )
        (i64.const 56)
       )
       (i64.const 56)
      )
     )
    )
    (set_local $8
     (i64.shl
      (i64.and
       (get_local $8)
       (i64.const 31)
      )
      (i64.and
       (get_local $5)
       (i64.const 4294967295)
      )
     )
    )
   )
   (set_local $4
    (i32.add
     (get_local $4)
     (i32.const 1)
    )
   )
   (set_local $6
    (i64.add
     (get_local $6)
     (i64.const 1)
    )
   )
   (set_local $7
    (i64.or
     (get_local $8)
     (get_local $7)
    )
   )
   (br_if $label$0
    (i64.ne
     (tee_local $5
      (i64.add
       (get_local $5)
       (i64.const -5)
      )
     )
     (i64.const -6)
    )
   )
  )
  (block $label$6
   (block $label$7
    (br_if $label$7
     (i64.ne
      (get_local $7)
      (get_local $1)
     )
    )
    (i32.store
     (tee_local $4
      (i32.add
       (get_local $9)
       (i32.const 24)
      )
     )
     (i32.const 0)
    )
    (i64.store offset=16
     (get_local $9)
     (i64.const 0)
    )
    (call $eosio_assert
     (i32.gt_u
      (call $read_action
       (i32.add
        (get_local $9)
        (i32.const 8)
       )
       (i32.const 20)
      )
      (i32.const 19)
     )
     (i32.const 64)
    )
    (set_local $2
     (i32.load
      (get_local $4)
     )
    )
    (set_local $3
     (i32.load8_u offset=16
      (get_local $9)
     )
    )
    (set_local $6
     (i64.load offset=8
      (get_local $9)
     )
    )
    (call $prints
     (i32.const 16)
    )
    (call $printn
     (get_local $6)
    )
    (call $prints
     (i32.const 32)
    )
    (call $prints
     (select
      (get_local $2)
      (i32.add
       (get_local $9)
       (i32.const 17)
      )
      (i32.and
       (get_local $3)
       (i32.const 1)
      )
     )
    )
    (br_if $label$6
     (i32.eqz
      (i32.and
       (i32.load8_u offset=16
        (get_local $9)
       )
       (i32.const 1)
      )
     )
    )
    (call $_ZdlPv
     (i32.load
      (get_local $4)
     )
    )
    (br $label$6)
   )
   (call $prints
    (i32.const 16)
   )
   (call $printn
    (get_local $0)
   )
   (call $prints
    (i32.const 96)
   )
   (call $printn
    (get_local $1)
   )
   (call $prints
    (i32.const 112)
   )
  )
  (i32.store offset=4
   (i32.const 0)
   (i32.add
    (get_local $9)
    (i32.const 32)
   )
  )
 )
 (func $_ZdlPv (param $0 i32)
  (block $label$0
   (br_if $label$0
    (i32.eqz
     (get_local $0)
    )
   )
   (call $free
    (get_local $0)
   )
  )
 )
 (func $free (param $0 i32)
  (local $1 i32)
  (local $2 i32)
  (local $3 i32)
  (block $label$0
   (block $label$1
    (br_if $label$1
     (i32.eqz
      (get_local $0)
     )
    )
    (br_if $label$1
     (i32.lt_s
      (tee_local $2
       (i32.load offset=8500
        (i32.const 0)
       )
      )
      (i32.const 1)
     )
    )
    (set_local $3
     (i32.const 8308)
    )
    (set_local $1
     (i32.add
      (i32.mul
       (get_local $2)
       (i32.const 12)
      )
      (i32.const 8308)
     )
    )
    (loop $label$2
     (br_if $label$1
      (i32.eqz
       (tee_local $2
        (i32.load
         (i32.add
          (get_local $3)
          (i32.const 4)
         )
        )
       )
      )
     )
     (block $label$3
      (br_if $label$3
       (i32.gt_u
        (i32.add
         (get_local $2)
         (i32.const 4)
        )
        (get_local $0)
       )
      )
      (br_if $label$0
       (i32.gt_u
        (i32.add
         (get_local $2)
         (i32.load
          (get_local $3)
         )
        )
        (get_local $0)
       )
      )
     )
     (br_if $label$2
      (i32.lt_u
       (tee_local $3
        (i32.add
         (get_local $3)
         (i32.const 12)
        )
       )
       (get_local $1)
      )
     )
    )
   )
   (return)
  )
  (i32.store
   (tee_local $3
    (i32.add
     (get_local $0)
     (i32.const -4)
    )
   )
   (i32.and
    (i32.load
     (get_local $3)
    )
    (i32.const 2147483647)
   )
  )
 )
)
