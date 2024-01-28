#' Create a new ValidationError
#'
#' @description
#' ValidationError Class
#'
#' @docType class
#' @title ValidationError
#' @description ValidationError Class
#' @format An \code{R6Class} generator object
#' @field loc  \link{AnyType}
#' @field msg  \link{AnyType}
#' @field type  \link{AnyType}
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
ValidationError <- R6::R6Class(
  "ValidationError",
  public = list(
    `loc` = NULL,
    `msg` = NULL,
    `type` = NULL,
    #' Initialize a new ValidationError class.
    #'
    #' @description
    #' Initialize a new ValidationError class.
    #'
    #' @param loc loc
    #' @param msg msg
    #' @param type type
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(`loc`, `msg`, `type`, ...) {
      if (!missing(`loc`)) {
        stopifnot(R6::is.R6(`loc`))
        self$`loc` <- `loc`
      }
      if (!missing(`msg`)) {
        stopifnot(R6::is.R6(`msg`))
        self$`msg` <- `msg`
      }
      if (!missing(`type`)) {
        stopifnot(R6::is.R6(`type`))
        self$`type` <- `type`
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return ValidationError in JSON format
    #' @export
    toJSON = function() {
      ValidationErrorObject <- list()
      if (!is.null(self$`loc`)) {
        ValidationErrorObject[["loc"]] <-
          self$`loc`$toJSON()
      }
      if (!is.null(self$`msg`)) {
        ValidationErrorObject[["msg"]] <-
          self$`msg`$toJSON()
      }
      if (!is.null(self$`type`)) {
        ValidationErrorObject[["type"]] <-
          self$`type`$toJSON()
      }
      ValidationErrorObject
    },
    #' Deserialize JSON string into an instance of ValidationError
    #'
    #' @description
    #' Deserialize JSON string into an instance of ValidationError
    #'
    #' @param input_json the JSON input
    #' @return the instance of ValidationError
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`loc`)) {
        `loc_object` <- AnyType$new()
        `loc_object`$fromJSON(jsonlite::toJSON(this_object$`loc`, auto_unbox = TRUE, digits = NA))
        self$`loc` <- `loc_object`
      }
      if (!is.null(this_object$`msg`)) {
        `msg_object` <- AnyType$new()
        `msg_object`$fromJSON(jsonlite::toJSON(this_object$`msg`, auto_unbox = TRUE, digits = NA))
        self$`msg` <- `msg_object`
      }
      if (!is.null(this_object$`type`)) {
        `type_object` <- AnyType$new()
        `type_object`$fromJSON(jsonlite::toJSON(this_object$`type`, auto_unbox = TRUE, digits = NA))
        self$`type` <- `type_object`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return ValidationError in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`loc`)) {
          sprintf(
          '"loc":
          %s
          ',
          jsonlite::toJSON(self$`loc`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`msg`)) {
          sprintf(
          '"msg":
          %s
          ',
          jsonlite::toJSON(self$`msg`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        },
        if (!is.null(self$`type`)) {
          sprintf(
          '"type":
          %s
          ',
          jsonlite::toJSON(self$`type`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
    },
    #' Deserialize JSON string into an instance of ValidationError
    #'
    #' @description
    #' Deserialize JSON string into an instance of ValidationError
    #'
    #' @param input_json the JSON input
    #' @return the instance of ValidationError
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`loc` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`loc`, auto_unbox = TRUE, digits = NA))
      self$`msg` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`msg`, auto_unbox = TRUE, digits = NA))
      self$`type` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`type`, auto_unbox = TRUE, digits = NA))
      self
    },
    #' Validate JSON input with respect to ValidationError
    #'
    #' @description
    #' Validate JSON input with respect to ValidationError and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
      # check the required field `loc`
      if (!is.null(input_json$`loc`)) {
        stopifnot(R6::is.R6(input_json$`loc`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for ValidationError: the required field `loc` is missing."))
      }
      # check the required field `msg`
      if (!is.null(input_json$`msg`)) {
        stopifnot(R6::is.R6(input_json$`msg`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for ValidationError: the required field `msg` is missing."))
      }
      # check the required field `type`
      if (!is.null(input_json$`type`)) {
        stopifnot(R6::is.R6(input_json$`type`))
      } else {
        stop(paste("The JSON input `", input, "` is invalid for ValidationError: the required field `type` is missing."))
      }
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of ValidationError
    #' @export
    toString = function() {
      self$toJSONString()
    },
    #' Return true if the values in all fields are valid.
    #'
    #' @description
    #' Return true if the values in all fields are valid.
    #'
    #' @return true if the values in all fields are valid.
    #' @export
    isValid = function() {
      TRUE
    },
    #' Return a list of invalid fields (if any).
    #'
    #' @description
    #' Return a list of invalid fields (if any).
    #'
    #' @return A list of invalid fields (if any).
    #' @export
    getInvalidFields = function() {
      invalid_fields <- list()
      invalid_fields
    },
    #' Print the object
    #'
    #' @description
    #' Print the object
    #'
    #' @export
    print = function() {
      print(jsonlite::prettify(self$toJSONString()))
      invisible(self)
    }
  ),
  # Lock the class to prevent modifications to the method or field
  lock_class = TRUE
)
## Uncomment below to unlock the class to allow modifications of the method or field
# ValidationError$unlock()
#
## Below is an example to define the print function
# ValidationError$set("public", "print", function(...) {
#   print(jsonlite::prettify(self$toJSONString()))
#   invisible(self)
# })
## Uncomment below to lock the class to prevent modifications to the method or field
# ValidationError$lock()

