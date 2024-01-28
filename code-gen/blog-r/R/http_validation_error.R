#' Create a new HTTPValidationError
#'
#' @description
#' HTTPValidationError Class
#'
#' @docType class
#' @title HTTPValidationError
#' @description HTTPValidationError Class
#' @format An \code{R6Class} generator object
#' @field detail  \link{AnyType} [optional]
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
HTTPValidationError <- R6::R6Class(
  "HTTPValidationError",
  public = list(
    `detail` = NULL,
    #' Initialize a new HTTPValidationError class.
    #'
    #' @description
    #' Initialize a new HTTPValidationError class.
    #'
    #' @param detail detail
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(`detail` = NULL, ...) {
      if (!is.null(`detail`)) {
        stopifnot(R6::is.R6(`detail`))
        self$`detail` <- `detail`
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return HTTPValidationError in JSON format
    #' @export
    toJSON = function() {
      HTTPValidationErrorObject <- list()
      if (!is.null(self$`detail`)) {
        HTTPValidationErrorObject[["detail"]] <-
          self$`detail`$toJSON()
      }
      HTTPValidationErrorObject
    },
    #' Deserialize JSON string into an instance of HTTPValidationError
    #'
    #' @description
    #' Deserialize JSON string into an instance of HTTPValidationError
    #'
    #' @param input_json the JSON input
    #' @return the instance of HTTPValidationError
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`detail`)) {
        `detail_object` <- AnyType$new()
        `detail_object`$fromJSON(jsonlite::toJSON(this_object$`detail`, auto_unbox = TRUE, digits = NA))
        self$`detail` <- `detail_object`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return HTTPValidationError in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`detail`)) {
          sprintf(
          '"detail":
          %s
          ',
          jsonlite::toJSON(self$`detail`$toJSON(), auto_unbox = TRUE, digits = NA)
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
    },
    #' Deserialize JSON string into an instance of HTTPValidationError
    #'
    #' @description
    #' Deserialize JSON string into an instance of HTTPValidationError
    #'
    #' @param input_json the JSON input
    #' @return the instance of HTTPValidationError
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`detail` <- AnyType$new()$fromJSON(jsonlite::toJSON(this_object$`detail`, auto_unbox = TRUE, digits = NA))
      self
    },
    #' Validate JSON input with respect to HTTPValidationError
    #'
    #' @description
    #' Validate JSON input with respect to HTTPValidationError and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of HTTPValidationError
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
# HTTPValidationError$unlock()
#
## Below is an example to define the print function
# HTTPValidationError$set("public", "print", function(...) {
#   print(jsonlite::prettify(self$toJSONString()))
#   invisible(self)
# })
## Uncomment below to lock the class to prevent modifications to the method or field
# HTTPValidationError$lock()

